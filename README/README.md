# ucdpa_django_project

https://ucdpa-django-project.onrender.com/

App to use API with authentication  - https://github.com/alglass0427/ucd_django_frontend_api

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

NOTE : DEBUG is set to false  - Changes may be required if Cloudinary is not used as storage

    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

makefile

    DEBUG='FALSE'
    DATABASE_URL='postgresql://alwglass:wa050J5ItIEvuS0Y2qwMVEMpqiKTSpLx@dpg-ct2dhktsvqrc73dsn8c0-a.oregon-postgres.render.com/projects_db_31e4'
    DJANGO_SUPERUSER_EMAIL= [email]
    DJANGO_SUPERUSER_PASSWORD= [password]
    DJANGO_SUPERUSER_USERNAME= [username]
    RENDER_HOSTNAME='ucdpa-django-project.onrender.com'
    SECRET_KEY='d4e5320356f82176a7d1b71cc44ec33a'
    # DATABASE_URL='postgresql://alwglass:wa050J5ItIEvuS0Y2qwMVEMpqiKTSpLx@dpg-ct2dhktsvqrc73dsn8c0-a.oregon-postgres.render.com/projects_db_31e4'
    CLOUD_NAME='dw32qih2n'
    API_KEY='426794781113865'
    API_SECRET='L1Wg6HqYJ_u0RWiGYCSAmvbPR-4'

environ is used to allow the programme to run locally -  using the .env file.

    import environ
    env = environ.Env()

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

# App Sample Features
## LOGIN /  USERS

![Login Screen](image.png)

### Forget Password - 

    from django.contrib.auth import views as auth_views

    urlpatterns += [
        path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"),name ='reset_password'),  ##,name ='reset_password'   <<---DEFAULT
        path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),name ='password_reset_done'),
        path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),name ='password_reset_confirm'), ## encode user id in base 64 
        path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="reset_password_complete.html"),name ='password_reset_complete') 

    ]

### Signals to create Profile when user is Created

    from django.db.models.signals import post_save ,  post_delete
     - - using signals with decorators
    from django.dispatch import receiver

    @receiver(post_save,sender = User)
    def createProfile(sender,instance,created, **kwargs):   ### create only exists if the Object is created in that instance
    print('Create Profile Signal triggered  . . . ')
    if created:                 # User is the Sender  -  so this checks if the User is created
        user = instance         #  
        profile = Profile.objects.create(
            user=user,
            username = user.username,
            email = user.email,
            name = user.first_name
        )

### Email - Send email when Account is created

    from django.core.mail import send_mail

    settings.py configured To store email server variables

    send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,

        )

## Projects 

![Projects](image-2.png)

### Search

Search functions using __icontains From "Q" import 
Sample

    projects = Project.objects.distinct().filter(
        Q(title__icontains = search_query)|
        Q(description = search_query)|
        Q(owner__name__icontains = search_query)|  ##two sets of double underscores is nested query
        Q(tags__in=tags)
    )

![Profile Search](image-1.png)


### Pagination

Display 3 projects at A time with options navigate through pages

    from django.core.paginator import Paginator , PageNotAnInteger, EmptyPage


### Reviews

Leave reviews on user projects - 

![Profile Search](image-4.png)

## Admin 

![Admin](image-5.png)

# API / API / Serializers

## Serializers
Example

    from rest_framework import serializers
    from projects.models import Project , Tag ,Review
    from users.models import Profile

    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = '__all__'


## Exposed API to fetch projects

API token required for POST / PUT 

    @api_view(['POST','PUT'])
    @permission_classes([IsAuthenticated])
    def projectVote (request , pk):
    
        project =  Project.objects.get(id=pk)
        user = request.user.profile
        data = request.data   ###NOTE .data is made available from the api_view decorator  - -- - BOD of DATA RECIEVED in SERIALIZED

        review , created =  Review.objects.get_or_create(
            owner = user,
            project=project,
        )

        review.value = data['value']
        review.save()
        project.getVoteCount   ###becase the @property decorator is used in the Project Model the () is not needed 

        print('DATA : ' , data)

        serializer =  ProjectSerializer(project,many=False)
        return Response(serializer.data)

When User is a logged in user 

![API](image-6.png)

![API - Token](image-7.png)


























