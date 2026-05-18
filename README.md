# The Vault - Photo Gallery Web Application

A Photo Gallery web application built using Django, PostgreSQL, and styled using Tailwind CSS. "The Vault" offers a fast, visually rich, and highly interactive user experience across all devices.


---

## Key Features

### User Authentication and Registration
- Fully secure signup and login flows utilizing Django's built-in cryptographic password hashing.
- Dual-identification custom auth backend (authenticate securely using username or email).


### Profile Management
- **Private Settings Dashboard**: Allows users to change their profile pictures (avatar), bio, edit their accounts, or securely change their passwords.
- **Public Profile Pages**: Every user gets an automatically generated public-facing profile page at /user/<username>/ showcasing their uploaded gallery and custom bio

### Photo Gallery Display and Logic
- **Interactive Grid**: Implements a sleek, responsive grid of photos featuring smooth hover transitions, tag lists, and direct like/dislike buttons.
- **CRUD Operations**: CRUD interfaces allowing owners to upload, modify, or delete their photos with authorization.

### Interactive Tag Filtering
- Fully interactive filter bar containing pre-populated categories (Nature, Architecture, Portrait, Landscape, Travel, Animals, Abstract, Street).


### Modern Interactions (Likes and Dislikes)
- Dual interactions with counters displaying on both the homepage and detail screens.
- Interactive states highlight green (likes) and red (dislikes) immediately upon toggle, clearing opposite states automatically.

---

## Tech Stack and Requirements
- **Backend Framework:** Django 6.0.5
- **Database Engine:** PostgreSQL
- **Styling System:** Pure Tailwind CSS
- **Version Control:** Git
- **Environment variables:** python-decouple

---

## Local Setup and Installation

Follow these steps to run the application locally on your machine:

### 1. Clone the Repository and Configure Directory
```bash
git clone <repository-url>
cd photo_gallery_app
```

### 2. Set Up Virtual Environment and Dependencies
- Ensure Python 3.x is installed:
```bash
# Create virtual env
python -m venv env
```

- Activate virtual env 
``` bash
# (WSL / Ubuntu / Linux)
source env/bin/activate

# (Windows)
.\env\Scripts\activate
```
- Install dependencies
``` bash
pip install -r requirements.txt
```

### 3. Setup PostgreSQL Database
Ensure a PostgreSQL server is running locally. Create a new database:
```sql
CREATE DATABASE photo_gallery_db;
```

### 4. Setup Environment Settings (.env)
Create a .env file in the root directory:
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
Visit the local site at http://127.0.0.1:8000/.

---

## Security Best Practices Implemented
- **Password Protection**: Built on top of Django's default PBKDF2 hashing engine.
- **CSRF Tokens**: Fully integrated across all POST forms (Registration, Login, Settings Update, Uploads, and Confirm Deletes) to prevent cross-site request forgery.
- **SQL Injection Prevention**: Using Django's built-in ORM parameterization.
- **Access Authorization Controls**: Session-level verification ensures only the upload owner has editing or deletion rights on resources.
