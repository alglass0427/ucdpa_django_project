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

# App Features
## LOGIN

![Login Screen](image.png)

Forget Password - 