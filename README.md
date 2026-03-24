<h1>Django 6 + Ninja + Nuxt 4 + Bootstrap 5</h1>

Example project showcasing API consumption from Django 6 + Django Ninja 
using Nuxt 4 + Bootstrap 5. Built as a reference implementation for developers
building full-stack JavaScript/Python applications with decoupled architecture.

<h2>Prerequisites</h2>

```
Python >= 3.12
Django == 6.0.2
django-ninja==1.5.3
django-cors-headers==4.9.0
Node.js >= v20.20.0
npm
```

<h2>Development Setup</h2>

Follow these steps to get the project running in your local development environment:

<h3>Backend Setup (Django)</h3>

Navigate to backend directory

```
$ cd backend
```

Install Python dependencies

```
$ pip install -r requirements.txt
```

Create your local settings file

```
$ cp backend/settings.py_example backend/settings.py
```

Run database migrations for the apps and create database

```
$ python manage.py makemigrations users products

$ python manage.py migrate
```

Start the Django development server

```
$ python manage.py runserver
```

<h3>Test the project:</h3>

Open your browser to http://127.0.0.1:8000 and you'll see the Django 6 CRUD
application for managing people records.

<h3>Test the API of Django Ninja:</h3>

Open your browser to: http://127.0.0.1:8000/api/docs

From that interface (Swagger), you can:

- View all your endpoints.

- Click "Test it" and test all the methods.

- Send a JSON object to create a person and see the response in real time.

- List people http://127.0.0.1:8000/api/person/

- Get people http://127.0.0.1:8000/api/person/{person_id}

<h3>Frontend Setup (Nuxt)</h3>

Open a new terminal and navigate to frontend directory

```
$ cd frontend
```

Install Node.js dependencies

```
$ npm install
```

Create your local settings file

```
$ cp .env_example .env
```

Start the Nuxt development server

```
$ npm run dev
```

The Nuxt application will be available at http://localhost:3000/

<h2>Access the Application</h2>

Once both servers are running:

Backend API: http://127.0.0.1:8000/api/person - Django Ninja person endpoint

Frontend: http://localhost:3000/ - View the initial project page
