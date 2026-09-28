# Mitalli Bridal World & Makeover Studio

A website + booking + lead-management system for Mitalli Bridal World & Makeover Studio
(Sangamner, Maharashtra), built per the project's MVP scope: services & pricing, bridal
packages, appointment requests, lead capture, a bilingual (English/Marathi) rule-based
chatbot, and an admin panel for the owner to manage everything without touching code.

## Stack

- **Backend:** FastAPI + SQLAlchemy + Jinja2 (server-rendered — one deployable service)
- **Database:** PostgreSQL in production (Render managed DB), SQLite for local dev
- **Chatbot:** Rule-based, reads live prices/packages from the database (no invented info)
- **Auth:** Simple session-based admin login (bcrypt-hashed passwords)

## Local development

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # edit as needed
uvicorn app.main:app --reload
```

Visit http://127.0.0.1:8000 — the app auto-creates tables and seeds initial data
(services, bridal packages, settings, one admin user) on first run.

Default admin login (change immediately): `admin` / `ChangeMe123!`
(or whatever you set in `.env`).

## Deploying to Render

See [`docs/DEPLOYMENT.md`](docs/DEPLOYMENT.md) — this repo includes a `render.yaml`
Blueprint for one-click deploy of both the web service and a managed Postgres database.

## Project structure

```
app/
├── main.py             # FastAPI app entrypoint
├── database.py         # SQLAlchemy engine/session
├── models.py           # Service, BridalPackage, Appointment, Lead, Review, SiteSetting, AdminUser
├── config.py           # Verified vs owner-to-confirm business info defaults
├── chatbot.py          # Rule-based bilingual chatbot
├── auth.py             # Password hashing + admin session check
├── seed.py             # Idempotent initial data seed
├── routers/
│   ├── public.py       # Home, About, Services, Bridal, Gallery, Reviews, Contact
│   ├── booking.py       # Booking form, contact lead form, chatbot API
│   └── admin.py         # Login, dashboard, CRUD for services/packages/appointments/leads/settings/reviews
├── templates/           # Jinja2 HTML (public site + admin/)
└── static/              # CSS, JS
render.yaml              # Render Blueprint (web service + Postgres)
docs/DEPLOYMENT.md        # Full deployment guide
```

## Data policy (see `app/config.py`)

Business facts came from two sources:
- **Verified/public** (Justdial listing): address, phone, established year, public hours,
  current rating — seeded as confirmed.
- **Owner-to-confirm**: an alternate rating, response time, alternate hours, exact bridal
  package inclusions/prices — seeded but flagged unconfirmed in the admin Settings page,
  and bridal packages start **unpublished** until confirmed.

## What's intentionally NOT built yet (see PROJECT_PLAN.md Sections 35–36)

- Advanced Marathi NLP / RAG-based chatbot (Version 3)
- WhatsApp Business API integration, automated email/SMS reminders (Version 2)
- Analytics dashboard, coupons, blog (Version 2)

The MVP is meant to ship first and prove the booking/lead pipeline before adding these.
