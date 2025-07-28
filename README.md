# 🔐 Django Authentication - Basic Login System

This is a **very basic Django web application** built to implement user authentication. It includes signup, login, logout, and protected views. The app demonstrates how to use Django's built-in `auth` system in a clean and beginner-friendly project structure.

---

## ✅ Features

- User **Signup** with form validation  
- User **Login** and **Logout**  
- Access-restricted **Home Page** after login  
- Simple use of **Django sessions and decorators**  
- Minimal HTML templates using Django templating system  

---

## 🛠️ Tech Stack

- **Backend**: Python, Django  
- **Frontend**: HTML, CSS (Bootstrap optional)  
- **Database**: SQLite (default)  
- **Tooling**: VS Code, Git

---

## 📁 Folder Structure

```plaintext
Django-Authentication-main/
├── authentication/               # Main app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                  # Signup/Login forms
│   ├── models.py
│   ├── urls.py                   # App-level routes
│   ├── views.py                  # View functions
│   ├── templates/
│   │   └── authentication/
│   │       ├── base.html
│   │       ├── signup.html
│   │       ├── login.html
│   │       └── home.html
│   └── migrations/
│       ├── __init__.py
│
├── django_auth/                 # Project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py              # Project settings
│   ├── urls.py                  # Root URL config
│   └── wsgi.py
│
├── db.sqlite3                   # SQLite database
├── manage.py                    # Django project runner
└── README.md                    # This file
```

---

## ⚙️ How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Django-Authentication.git
cd Django-Authentication-main
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate         # Windows: venv\Scripts\activate
```

### 3. Install Django
```bash
pip install django
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Start the Server
```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/`

---

## 📌 Default Routes

- `/signup` – Register a new user  
- `/login` – Log in an existing user  
- `/logout` – Log out the current session  
- `/` – Home page (login required)

---

This project serves as a minimal and clean starting point for building user-authenticated Django applications.
