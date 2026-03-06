# 🧾 Django DevOps Notes App (Dockerized)

A simple **DevOps Notes Manager** built using **Django** and **Docker**.  
This project lets you store and view DevOps commands in a clean web interface.

It demonstrates a **basic DevOps workflow** including:

- Django backend development
- Database modeling
- Docker containerization
- Git version control
- GitHub repository management
- DockerHub image distribution

---

# 🚀 Features

- Create and manage DevOps command notes
- Django Admin panel for managing notes
- Web interface to display notes
- Docker containerized application
- GitHub project repository
- Clean project structure
- `.gitignore` protection for sensitive files

---

# 🏗 Architecture

```
User Browser
     │
     ▼
Django Application
     │
     ▼
SQLite Database
```

Application runs inside a **Docker container**.

---

# 📁 Project Structure

```
django-notes-app
│
├── Dockerfile
├── requirements.txt
├── manage.py
├── .gitignore
├── README.md
│
├── devops/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── notes/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── tests.py
    │
    ├── migrations/
    │   └── 0001_initial.py
    │
    └── templates/
        └── notes/
            └── list.html
```

---

# ⚙️ Local Installation

## 1 Clone the Repository

```bash
git clone https://github.com/wasimat404/django-notes-app-docker-friendly.git
```

```
cd django-notes-app-docker-friendly
```

---

## 2 Install Dependencies

```
pip install -r requirements.txt
```

---

## 3 Run Database Migrations

```
python manage.py migrate
```

---

## 4 Create Admin User

```
python manage.py createsuperuser
```

---

## 5 Run Development Server

```
python manage.py runserver 0.0.0.0:8000
```

---

# 🌐 Access the Application

Open in browser:

```
http://SERVER_IP:8000
```

Admin panel:

```
http://SERVER_IP:8000/admin
```

Login using the **superuser credentials**.

---

# 📝 Creating DevOps Notes

Inside Admin Panel:

```
Admin → Notes → Add Note
```

Example note:

Title
```
Docker Cleanup
```

Command
```
docker system prune -a
```

Tag
```
docker
```

---

# 🐳 Docker Containerization

This project can run completely inside a Docker container.

---

# Build Docker Image

Run inside the project directory:

```
docker build -t django-notes .
```

---

# Run Docker Container

```
docker run -d -p 8000:8000 django-notes
```

Open in browser:

```
http://SERVER_IP:8000
```

---

# 📦 DockerHub Image

DockerHub repository:

```
https://hub.docker.com/r/zenew/django-notes
```

Run directly from DockerHub:

```
docker run -d -p 8000:8000 zenew/django-notes
```

---

# 🔒 Security

Sensitive files are excluded using `.gitignore`.

Ignored files:

```
db.sqlite3
__pycache__/
.env
```

This prevents local data and secrets from being pushed to GitHub.

---

# 🧰 Tech Stack

- Python
- Django
- SQLite
- Docker
- Git
- GitHub

---

# 📚 DevOps Concepts Demonstrated

- Docker image building
- Containerized application deployment
- Git version control workflow
- GitHub repository management
- Ignoring sensitive files
- Basic backend web development

---

# 👨‍💻 Author

Wasim Akram

GitHub  
```
https://github.com/wasimat404
```

DockerHub  
```
https://hub.docker.com/r/zenew
```

---

# ⭐ Future Improvements

- PostgreSQL database
- Docker Compose setup
- CI/CD pipeline with GitHub Actions
- Production deployment with Nginx + Gunicorn
- Notes search and tag filtering
