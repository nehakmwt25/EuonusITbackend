# Euonus IT Backend

Django + Django REST Framework API for the Euonus IT website. The project uses SQLite by default and accepts a PostgreSQL `DATABASE_URL` in production.

## Setup

```bash
cd Backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Admin is available at `http://127.0.0.1:8000/admin/`. Add active website content and job openings there before using the public pages.

The React frontend runs on port 5173 and proxies `/api` to Django during development. Set `VITE_API_URL` when the API is hosted elsewhere.

## API

Public GET endpoints: `/api/services/`, `/api/it-services/`, `/api/why-choose-us/`, `/api/industries/`, `/api/clients/`, `/api/projects/`, `/api/projects/featured/`, `/api/testimonials/`, `/api/awards/`, `/api/companies/`, `/api/careers/`, `/api/blogs/`, `/api/blogs/latest/`, `/api/faqs/`.

Filters include `/api/clients/?industry=<slug>`, `/api/blogs/?category=<name>`, `/api/blogs/?search=<term>`, and `/api/faqs/?category=<name>`.

Public POST endpoints are `/api/contact/`, `/api/faq-query/`, and `/api/careers/<slug>/apply/`. Contact and FAQ query responses never expose internal status fields. Resume uploads accept PDF/DOC/DOCX files up to 5 MB.

## Environment

`SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS`, and `DATABASE_URL` are read from `.env`. Uploaded files are stored in `media/`; collected static files go to `staticfiles/`.
