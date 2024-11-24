"""
URL configuration for schoolConnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# def homePage(request):
#     return HttpResponse('<h1>Hello World</h1>')


def homePage(request):
    return HttpResponse('Home Page!!')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),   #     add user urlpatterns

    
    path('', include('users.urls')),   #   add user urlpatterns --->>>> first paramater is the route , http://127.0.0.1:8000/<ROUTE>  
            ###above will default To path('',views.profiles,name="profiles") from sers/urls.py
    path('api/', include('api.urls')),
    # path('reset_password/', auth_views.PasswordResetView.as_view(),name ='reset_password'),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name ='password_reset_done')
]

### += apending to the URLPATTERNS to seperate concerns
###static(()) is the Metod imported above 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


###VIEWS CLASS -  View Models



####RESET PASSWORD -  USES SETTINGS .py for EMAIL SETTINGS
urlpatterns += [
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"),name ='reset_password'),  ##,name ='reset_password'   <<---DEFAULT
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),name ='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),name ='password_reset_confirm'), ## encode user id in base 64 
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"),name ='password_reset_complete') 

]