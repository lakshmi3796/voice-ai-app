1. Create a main project folder-
   - mkdir <project_folder_name>
2. Create a backend djnago project folder-
   - mkdir <backend_django_project_folder_name>
3. Create a frontend project folder-
   - mkdir <backend_fastapi_project_folder_name>
4. Create a virtual environment using python inside fastapi folder -
  - python3 -m venv <env_name>
5. Create a virtual environment using python for backend inside backend-django folder -
  - python3 -m venv <env_name>
6. Activate virtual environment (for backend goto inside backend-django folder and same for fastapi goto inside backend-fatsapi folder) after that run below command)-
   - source env/bin/activate
7. Install module registered in requirements.txt via pip-(for backend goto inside backend-django folder and same for fastapi goto inside backend-fatsapi folder) after that run below command)
   - pip install -r requirements.txt

### For backend ###

8. Create django project inside backend-django folder-
   - django-admin startproject <project_name>
9. Goto inside project folder-
  - cd <project_name>
10. Create django app-
  - python manage.py startapp <app_name>
11. Register your app in your django project's settings.py inside INSTALLED_APPS-
  - INSTALLED_APPS[...,<app_name>,]
12. Add models as per project requirements in django_app/models.py-
  - Conversation
13. After that migrate db-
  - python manage.py makemigrations
  - python manage.py migrate
14. Run the server-
  - python manage.py runserver
15. Create superuser/admin-
  - python manage.py createsuperuser

16. Run fastAPI server-
    -uvicorn main:app --reload --port 8001

### For frontend ###

17. Install nodejs (macOS)---
    -brew install node
18. Install npm(for reactJs)-
    -npm install
19. Start reactjs development server-
    -npm start
20. Create a React app in the frontend folder-
    -npx create-react-app frontend
21. Update App.js file according your project requirement.


** Basic server start at localhost:8000 **
