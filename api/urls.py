from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,   ###GENERATE TOKEN
    TokenRefreshView,      ###GIVE A TOKEN TO GENERATE A NEW TOKEN -  longer expiration
)

urlpatterns =[
    path('',views.getRoutes),
    path('projects/',views.getProjects),
    path('projects/<str:pk>',views.getProject),
    path('projects/<str:pk>/vote/',views.projectVote)

]

##REST URLS FOR API
urlpatterns += [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
]