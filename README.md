# GmapDjango

**Getting Started**

Setup project environment with virtualenv and pip.
 
 $ virtualenv project-env

$ source project-env/bin/activate 

$ pip install -r requirements.txt 


# Start project

$ django-admin startproject projectname

$ cd projectname/

$ python manage.py migrate

$ python manage.py runserver

**To create an superuser account, use this command:**

$ python manage.py createsuperuser

**Features**

Python/ Django/ Django Rest Framework/Postgres/ Google Apis

Google apis: https://console.cloud.google.com/

Admin Dashboard

http://127.0.0.1:8000/admin/


**Tests**

To run the tests, cd into the directory where manage.py is:

(env)$ python manage.py test map
