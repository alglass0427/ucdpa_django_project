from django.urls import path
from . import views

urlpatterns = [
    # path('projects/', views.projects ,  name = "projects"),
    path('', views.projects ,  name = "projects"), # make projects.html as home
    path('project/<str:pk>', views.project ,  name = "project"),  #### --->>> add <str:pk> the url parameter and To the def function above
    path('create-project/', views.createProject , name= "create-project"),
    path('update-project/<str:pk>/', views.updateProject , name= "update-project"),
    path('delete-project/<str:pk>/', views.deleteProject , name= "delete-project")
]
