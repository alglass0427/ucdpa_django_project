# ucdpa_django_project

## School Project Display Application with PostgreSQL

An application built using the Django Framework in Python for Students to create an Account / Display Projects and recieve feedback / reviews


## Features
User Authentication: Secure login and session management.
Profile Management: Add, Edit and View Accounts /  Profiles.
Project Management: Add, Edit and View Projects related to individual Projects.
Upload and Display images -  storage in Cloudinary.
Send Messages between users , logged in and guests to the app.
API -  Exposed for Project details with json respons of Projects / Owners
Tested via Postman and External HTML/CSS/JS basic app to allow voting on projects
Responsive UI: A downloeded UI template for responsive interface that adapts to different screen sizes.

## Prerequisites
Before running this application, ensure you have the following installed:

Python 3.x
pip

# Installation
## Clone the Repository

    git clone https://github.com/alglass0427/ucdpa_django_project

## Create and Activate a Virtual Environment

Create a virtual environment to manage dependencies:

    python -m venv venv

Activate the virtual environment:
Windows:
    venv\Scripts\activate

macOS/Linux:
    source venv/bin/activate

## Install Dependencies
Install all required Python packages using requirements.txt:
    pip install -r requirements.txt

## Set Up Environment Variables

Create a .env file in the root directory of the project and add the following environment variables:

makefile

    DEBUG='FALSE'
    DATABASE_URL='postgresql://alwglass:wa050J5ItIEvuS0Y2qwMVEMpqiKTSpLx@dpg-ct2dhktsvqrc73dsn8c0-a.oregon-postgres.render.com/projects_db_31e4'
    DJANGO_SUPERUSER_EMAIL='alwglass@gmail.com'
    DJANGO_SUPERUSER_PASSWORD='Holly0427'
    DJANGO_SUPERUSER_USERNAME='alwglass'
    RENDER_HOSTNAME='ucdpa-django-project.onrender.com'
    SECRET_KEY='d4e5320356f82176a7d1b71cc44ec33a'
    # DATABASE_URL='postgresql://alwglass:wa050J5ItIEvuS0Y2qwMVEMpqiKTSpLx@dpg-ct2dhktsvqrc73dsn8c0-a.oregon-postgres.render.com/projects_db_31e4'
    CLOUD_NAME='dw32qih2n'
    API_KEY='426794781113865'
    API_SECRET='L1Wg6HqYJ_u0RWiGYCSAmvbPR-4'


## Initialize the Application
You may need to initialize some data or perform migrations (if applicable). If not, you can skip this step.

    python manage.py makemigrations
    python manage.py migrate
    python manage.py collectstatic

## DB Entries can be checked in DBMS If running locally in SQL Lite
    Open DB Browser For SQLLite
    
    select * from users_profile
    select * from projects_project

## Application Structure of SchoolConnect Project

    schoolConnect/
        schoolConnect/
        users/
        api/
        projects/

## Run Application

    python manage.py runserver

# Sample App Features
## LOGIN

![Login Screen](image.png)

### User Model
    from django.contrib.auth.models import User

### Signals to Create Profile on Creation of User
    from django.db.models.signals import post_save, post_delete
    from django.dispatch import receiver

    def createProfile(sender,instance,created, **kwargs):   ### create only exists if the Object is created in that instance
    print('Create Profile Signal triggered  . . . ')
    if created:                 # User is the Sender  - this checks if the User is created
        user = instance         #  
        profile = Profile.objects.create(
            user=user,
            username = user.username,
            email = user.email,
            name = user.first_name
        )
### Send Mail on user creation

    from django.core.mail import send_mail

        subject = 'Welcome to the Website'
        message = "Glad you joined -  Hope you enjoy"

        '''Variables from settings.py for email host etc'''    
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,

        )
### Features Reset Password

    from django.contrib.auth import views as auth_views
    urlpatterns += [
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"),name ='reset_password'),  ##,name ='reset_password'   <<---DEFAULT
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),name ='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),name ='password_reset_confirm'), ## encode user id in base 64 
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"),name ='password_reset_complete') 
    ]

## Profiles
### Search
    Search Functions to use filter with __icontains

    skills = Skill.objects.filter(name__icontains = search_query)
    
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains = search_query)| ##__icontains is is not case sensitive -->> BEFORE THE __icontains the filed vlaue from the table is entered  -  in this case "name"
        Q(short_intro__icontains = search_query)|
        Q(bio__icontains = search_query)|
        Q(skill__in=skills)

    from django.db.models import Q

    ![Search](image-1.png)

### Pagination
    from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage

## Projects

    consistant theme with Profiles -  display Projects With Search And Pgination

    ![Projects](image-2.png)

    Links To click to each Project

### Reviews 

    Leave Reviews for Each Project with ability to give feedback votes and Show the user that commented

    ![Reviews](image-4.png)

## Send Meassges

    Send Meassages to other users

## Admin

    ![Admin](image-5.png)

## API

    Exposed REST API to Fetch Project Details
    Allows POST And PUT methods where user is authenticated.

        from rest_framework.decorators import api_view , permission_classes
        from rest_framework.response import Response
        from rest_framework.permissions import IsAuthenticated ,

    ![API](image-6.png)

    ![API Token](image-7.png)

