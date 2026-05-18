# The Vault — Premium Photo Gallery Web Application

A premium, state-of-the-art Photo Gallery web application built using **Django**, **PostgreSQL**, and styled from scratch using pure **Tailwind CSS**. "The Vault" offers a fast, visually rich, and highly interactive user experience across all devices.

## 🚀 Live Site Link
* **Live Demo URL:** [https://photo-gallery-app-isaac.onrender.com](https://photo-gallery-app-isaac.onrender.com) *(Placeholder - update with your actual Render URL)*

---

## ✨ Key Features

### 🔒 User Authentication & Registration
- Fully secure signup and login flows utilizing Django’s built-in cryptographic password hashing.
- Dual-identification custom auth backend (authenticate securely using username or email).
- Complete session management, secure CSRF protection, and custom validation error messaging.

### 👤 Profile Management
- **Private Settings Dashboard**: Accessible strictly via `login_required` controls. Allows users to change their profile pictures (avatar), bio, edit their accounts, or securely change their passwords.
- **Public Profile Pages**: Every user gets an automatically generated public-facing profile page at `/user/<username>/` showcasing their uploaded gallery and custom bio, allowing read-only content discovery.

### 🖼️ Premium Photo Gallery Display & Logic
- **Interactive Grid**: Implements a sleek, responsive grid of photos featuring smooth hover transitions, tag lists, and direct like/dislike buttons.
- **Split-Pane Detail View**: Visual split screen showing high-resolution images alongside full details (owner cards, tags list, publication dates, and description).
- **CRUD Operations**: Secure CRUD interfaces allowing owners to upload, modify, or delete their photos with strict server-side authorization check boundaries.

### 🏷️ Interactive Tag Filtering
- Fully interactive filter bar containing premium pre-populated categories (*Nature, Architecture, Portrait, Landscape, Travel, Animals, Abstract, Street*).
- Highlight-active states designed as clickable pill badges for optimal navigation.

### 👍 Modern Interactions (Likes & Dislikes)
- YouTube-style dual interactions with counters displaying on both the homepage and detail screens.
- Interactive states highlight green (likes) and red (dislikes) immediately upon toggle, clearing opposite states automatically.

---

## 🛠️ Tech Stack & Requirements
- **Backend Framework:** Django 6.0.5
- **Database Engine:** PostgreSQL
- **Styling System:** Pure Tailwind CSS (integrated via official CDN)
- **Version Control:** Git
- **Configuration Security:** python-decouple (environment files)

---

## 💻 Local Setup & Installation

Follow these steps to run the application locally on your machine:

### 1. Clone the Repository & Configure Directory
```bash
git clone <your-repository-url>
cd photo_gallery_app
```

### 2. Set Up Virtual Environment & Dependencies
Ensure Python 3.x is installed:
```bash
# Create virtual env
python -m venv env

# Activate virtual env (WSL / Ubuntu / Linux)
source env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Setup PostgreSQL Database
Ensure a PostgreSQL server is running locally. Create a new database:
```sql
CREATE DATABASE photo_gallery_db;
```

### 4. Setup Environment Settings (`.env`)
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-custom-django-secret-key
DEBUG=True
DATABASE_NAME=photo_gallery_db
DATABASE_USER=postgres
DATABASE_PASSWORD=your-postgres-password
DATABASE_HOST=127.0.0.1
DATABASE_PORT=5432
```

### 5. Generate and Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Seed Default Category Tags
We have included a seed routine to prepopulate standard photography tags. Start the Django shell:
```bash
python manage.py shell
```
Then run this script inside the shell:
```python
from gallery.models import Tag
tags = ['Nature', 'Architecture', 'Portrait', 'Landscape', 'Travel', 'Animals', 'Abstract', 'Street']
for name in tags:
    Tag.objects.get_or_create(name=name)
print("Seeding successful!")
exit()
```

### 7. Run the Local Server
```bash
python manage.py runserver
```
Visit the local site at `http://127.0.0.1:8000/`.

---

## 🌐 Render Deployment Guide

Follow these simple guidelines to host the project live on [Render](https://render.com):

### 1. Database Creation
- Set up a **New PostgreSQL Database** on Render.
- Copy the **Internal Database URL** or **External Database URL**.

### 2. Configure Static Files (WhiteNoise)
Render requires static assets to be served securely. Add `whitenoise` to your `requirements.txt`:
```txt
whitenoise>=6.0.0
```
Update your `settings.py` middleware section:
```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Place right under security middleware
    ...
]
```

### 3. Deploy Web Service
- Link your Git Repository to Render.
- Select **Web Service**.
- Select environment: **Python 3**.
- Set **Build Command**:
  ```bash
  pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
  ```
- Set **Start Command**:
  ```bash
  gunicorn galleryproject.wsgi:application
  ```

### 4. Setup Render Environment Variables
Add these keys under the Service settings on Render:
- `SECRET_KEY` = your-production-secret-key
- `DEBUG` = `False`
- `DATABASE_NAME` = (Extract from your Render database credentials)
- `DATABASE_USER` = (Extract from your Render database credentials)
- `DATABASE_PASSWORD` = (Extract from your Render database credentials)
- `DATABASE_HOST` = (Extract from your Render database credentials)
- `DATABASE_PORT` = `5432`

---

## 🛡️ Security Best Practices Implemented
- **Password Protection**: Built on top of Django's default PBKDF2 hashing engine.
- **CSRF Tokens**: Fully integrated across all POST forms (Registration, Login, Settings Update, Uploads, and Confirm Deletes) to prevent cross-site request forgery.
- **SQL Injection Prevention**: Using Django’s built-in ORM parameterization.
- **Access Authorization Controls**: Session-level verification ensures only the upload owner has editing or deletion rights on resources.
