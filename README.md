# Directory - Django

Introduction:
-------------
This is a web application where the user can individually add or bulk upload the teachers profile using a `.csv` file.

Configuration:
--------------
1. asgiref==3.2.10
2. Django==3.0.8
3. django-crispy-forms==1.9.2
4. django-multiselectfield==0.1.12
5. Pillow==7.2.0
6. pytz==2020.1
7. sqlparse==0.3.1
8. Python - 3.8

Steps to launch the Application:
--------------------------------
1. Launch cmd(in Windows) or Terminal (in MacOS).
2. Run the command to clone the repo in local folder - `git clone https://github.com/mejaz/Directory.git`
3. Navigate inside `Directory` - `cd Directory`
4. Run the command `pipenv install -r requirements.txt` to install the dependencies.
5. Run `pipenv shell` to enter the virtual environment.
6. Navigate to the `school` directory by running command - `cd school`
7. Run command - `python manage.py migrate` to create the applicaiton tables in SQLiteDB.
8. Create a super user, as the application has login feature - `python manage.py createsuperuser`
9. Start the server - `python manage.py runserver`
10. The application will start running at - `http://127.0.0.1:8000/`

Contact me:
-----------
mohdejazsiddiqui@gmail.com
