# Django E-Commerce (Demo)

This is a demo Django e-commerce application (templates + Django backend). It is built to be edited in the GitHub web UI and deployed to Render.

## Quick start (local)
1. Create virtualenv, install requirements (`pip install -r requirements.txt`)
2. Copy `.env.example` to `.env` and set SECRET_KEY and DEBUG=True for local.
3. `python manage.py migrate`
4. `python manage.py createsuperuser`
5. `python manage.py runserver`

## Deploy to Render
- Create a new Web Service on Render from this GitHub repo.
- Use the `web: gunicorn ecom_project.wsgi` command (Procfile provided).
- Set the following environment variables in Render:
  - `SECRET_KEY` (set a secure value)
  - `DEBUG` = `False`
  - Optional: `DATABASE_URL` (if using Postgres)
  - `EMAIL_BACKEND` (if you want SMTP)
- Enable automatic deploys from main branch.

## Features
- Product categories & product detail
- Session-based cart
- Checkout (demo assumes paid)
- Order history
- Authentication (register/login)
- Simple REST API (Django REST Framework)
- Admin interface

This is a demo starter. Extend it with production payment integration (Razorpay/Stripe), image hosting, search, caching, and user addresses.
