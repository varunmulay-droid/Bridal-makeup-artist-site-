# Mitalli Bridal World & Makeover Studio
## Complete Website + AI Chatbot + Booking & Lead Management System

**Project Type:** Business Website + Customer Chatbot + Lead Generation + Appointment Management  
**Business:** Mitalli Bridal World & Makeover Studio  
**Location:** Near Mantri Bank, Nashik Road, Sangamner, Maharashtra 422605  
**Primary Audience:** Brides, women seeking beauty/skincare/hair services, festive customers, local Sangamner customers

---

# 1. PROJECT OBJECTIVE

Build a modern, mobile-first website for Mitalli Bridal World that:

1. Presents the salon professionally.
2. Showcases bridal makeup and beauty services.
3. Displays services and pricing.
4. Allows customers to request appointments.
5. Provides instant answers through a Marathi/English chatbot.
6. Captures customer leads.
7. Allows the owner/staff to manage inquiries.
8. Provides direct Call and WhatsApp actions.
9. Displays location and directions.
10. Provides a foundation for future online booking and CRM functionality.

The website should function as a **digital salesperson + customer-support assistant + lead collection system**.

---

# 2. IMPORTANT DATA POLICY

There are multiple sources containing different business information.

## VERIFIED/PUBLIC INFORMATION

The current public listing indicates:

- Established: 2006
- Location: Near Mantri Bank, Nashik Road, Sangamner
- Phone: 07383099084
- Services include hair styling, hair extensions, hair straightening, pedicure, manicure, artificial nail extensions, body waxing, basic makeup, bridal package and bridal makeup.
- Publicly listed hours: Monday–Saturday 9:30 AM–6:30 PM; Sunday closed.
- Current Justdial rating shown: 3.8/5 from 4 ratings.

Source: https://www.justdial.com/Sangamner/Mitalli-Bridal-World-Near-Mantri-Bank-Sangamner/9999PX241-X241-150312182233-A6B6_BZDET

## OWNER-CONFIRMATION DATA

The following supplied information should be confirmed with the owner before publishing:

- 4.7/5 rating
- 35+ minute average response time
- 10 AM–8 PM opening hours
- Exact service prices
- Hydra Facial
- Hair Spa
- Keratin
- Saree Draping
- Nail Art
- Pre-bridal packages
- Exact bridal package inclusions

Create an admin configuration so the owner can update these values without modifying source code.

---

# 3. WEBSITE GOALS

## Primary Goal

Convert:

```text
Inquiry
   ↓
Lead
   ↓
Appointment Request
   ↓
Confirmed Appointment
   ↓
Customer
```

## Secondary Goals

- Increase trust
- Show work/portfolio
- Make prices easier to understand
- Reduce repetitive questions
- Capture WhatsApp leads
- Improve response time
- Build a reusable customer database

---

# 4. TARGET USERS

### Bride
Needs bridal makeup, HD/Airbrush makeup, pre-bridal treatment, hair styling, saree draping and appointments.

### Regular Beauty Customer
Needs facial, cleanup, hair spa, waxing, threading, nails and hair treatments.

### Festival/Event Customer
Needs makeup, hairstyling, facial and nail services.

### Information-Seeking Customer
Asks about location, timings, prices, bridal makeup, appointments and home service.

---

# 5. WEBSITE STRUCTURE

```text
/
├── Home
├── About
├── Services
│   ├── Bridal Makeup
│   ├── Facial & Skincare
│   ├── Hair Care
│   ├── Nails
│   ├── Waxing & Threading
│   └── Other Services
├── Bridal Packages
├── Gallery
├── Reviews
├── Booking
├── Contact
└── Admin
```

---

# 6. HOME PAGE

## Hero

Headline:

> Your Beauty. Your Special Day. Your Perfect Look.

Subheading:

> Professional bridal makeup, skincare, hair care and beauty services in Sangamner.

Buttons:

```text
[ Book Appointment ]
[ WhatsApp Us ]
[ View Services ]
```

Design:

- Full-width bridal visual
- Elegant typography
- Premium, warm aesthetic
- Mobile-first
- Minimal animation

Avoid excessive animations, clutter and cheap-looking gradients.

---

# 7. TRUST SECTION

Potential structure:

```text
20+ Years of Experience
        |
Professional Beauty Services
        |
Bridal Makeup
        |
Sangamner Location
```

Confirm wording with owner before publishing. Public listing indicates establishment in 2006.

---

# 8. ABOUT SECTION

Heading:

> About Mitalli Bridal World

Explain:

- Established salon in Sangamner
- Bridal makeup specialization
- Beauty and personal-care services
- Local customer focus
- Professional service
- Personalized beauty consultations

CTA:

```text
[ Learn More ]
```

---

# 9. SERVICES

Each service card:

```text
Image
Service Name
Short Description
Duration
Starting Price
[Enquire]
```

Categories:

## Bridal Makeup

- Classic Bridal Makeup
- HD Bridal Makeup
- Airbrush Bridal Makeup
- Bridal Package

Supplied baseline prices:

```text
Classic Bridal Makeup      ₹12,000
HD/Airbrush Package        ₹18,000
```

Owner confirmation required.

## Facial & Skincare

- Cleanup
- Fruit Facial
- Gold Facial
- Hydra Facial
- Pre-Bridal Skincare

Supplied baseline:

```text
Cleanup                    ₹500
Fruit/Gold Facial          ₹1,200
Advanced Hydra Facial      ₹3,500
```

## Hair Care

- Hair Spa
- Hair Nourishment
- Hair Smoothening
- Keratin
- Hair Styling
- Hair Extension
- Hair Straightening

Supplied baseline:

```text
Hair Spa                   ₹999
Smoothening/Keratin        ₹4,500
```

## Nails

- Manicure
- Pedicure
- Nail Extensions
- Nail Art

## Hair Removal

- Waxing
- Threading
- Full Waxing/Threading Package

Supplied baseline:

```text
Waxing + Threading Package ₹800
```

## Styling

- Saree Draping
- Hair Styling
- Event Makeup

All supplied prices require owner confirmation.

---

# 10. SERVICE DATABASE

```sql
CREATE TABLE services (
    id SERIAL PRIMARY KEY,
    category VARCHAR(100) NOT NULL,
    name VARCHAR(150) NOT NULL,
    description TEXT,
    duration_minutes INTEGER,
    price INTEGER,
    price_type VARCHAR(30) DEFAULT 'fixed',
    image_url TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

`price_type`:

```text
fixed
starting_from
custom
on_request
```

This is important because bridal pricing may vary.

---

# 11. BRIDAL PACKAGES

Make this one of the most visually attractive sections.

Example:

```text
CLASSIC BRIDAL

₹12,000

• Bridal Makeup
• Professional Finish
• Personalized Look

[ Enquire Now ]
```

```text
HD / AIRBRUSH PREMIUM

₹18,000

• HD/Airbrush Makeup
• Premium Bridal Finish
• Personalized Styling

[ Enquire Now ]
```

Do not publish package inclusions until owner confirmation.

---

# 12. GALLERY

Categories:

```text
All
Bridal Makeup
Hair
Makeup
Skincare
Nails
Studio
```

Features:

- Lazy loading
- Lightbox
- Mobile swipe
- Category filters

Use genuine business images only.

---

# 13. REVIEWS

Display genuine customer reviews only.

```sql
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(150),
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    service VARCHAR(150),
    is_featured BOOLEAN DEFAULT FALSE,
    is_approved BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Never manufacture reviews.

---

# 14. LOCATION & CONTACT

Display:

```text
Mitalli Bridal World

Near Mantri Bank
Nashik Road
Sangamner
Maharashtra – 422605

Phone: 07383099084
```

Buttons:

```text
[ Get Directions ]
[ Call Now ]
[ WhatsApp ]
[ Book Appointment ]
```

Confirm the exact map pin with the owner.

---

# 15. APPOINTMENT SYSTEM

Start with an appointment request instead of complex real-time calendar synchronization.

Customer fields:

```text
Name
Phone
Service
Preferred Date
Preferred Time
Additional Message
```

Statuses:

```text
Pending
Contacted
Confirmed
Completed
Cancelled
```

Database:

```sql
CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(150) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    service_id INTEGER REFERENCES services(id),
    appointment_date DATE,
    preferred_time TIME,
    message TEXT,
    status VARCHAR(30) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Important: submitting a request must not imply the appointment is confirmed.

---

# 16. LEAD MANAGEMENT

Every inquiry should become a lead.

```sql
CREATE TABLE leads (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150),
    phone VARCHAR(20),
    source VARCHAR(50),
    service_interest VARCHAR(150),
    message TEXT,
    status VARCHAR(30) DEFAULT 'new',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Sources:

```text
website
chatbot
whatsapp
phone
instagram
google
justdial
```

---

# 17. CHATBOT

Goal: lightweight chatbot without paid LLM APIs.

Architecture:

```text
User
 ↓
Chat Widget
 ↓
FastAPI
 ↓
Preprocessing
 ↓
Intent Detection
 ↓
Service/Database Lookup
 ↓
Response
```

Intents:

```text
greeting
service_search
price_inquiry
booking_request
location
timings
home_service
bridal
contact
fallback
```

---

# 18. MULTILINGUAL SUPPORT

Initial support:

English:

```text
What is the price of Hydra Facial?
```

Marathi:

```text
Hydra facial कितीला आहे?
```

Marathi-English:

```text
Hydra facial cha rate kay aahe?
```

Normalize common variations.

---

# 19. CHATBOT BOOKING FLOW

```text
User:
"मला bridal makeup book करायचा आहे"

        ↓

Bot asks name
        ↓
Phone
        ↓
Preferred date
        ↓
Preferred time
        ↓
Database
        ↓
Lead / appointment request created
        ↓
Admin notification
```

The bot must retrieve prices from the database rather than hard-coding them.

---

# 20. BACKEND

Recommended:

```text
Python
FastAPI
SQLAlchemy
PostgreSQL
Pydantic
```

Structure:

```text
backend/
├── app/
│   ├── main.py
│   ├── models/
│   │   ├── service.py
│   │   ├── lead.py
│   │   ├── appointment.py
│   │   └── review.py
│   ├── schemas/
│   │   ├── service.py
│   │   ├── lead.py
│   │   └── appointment.py
│   ├── routes/
│   │   ├── services.py
│   │   ├── chatbot.py
│   │   ├── leads.py
│   │   ├── appointments.py
│   │   └── reviews.py
│   ├── chatbot/
│   │   ├── preprocessing.py
│   │   ├── intents.py
│   │   ├── patterns.py
│   │   └── engine.py
│   └── database.py
├── requirements.txt
└── .env
```

---

# 21. FRONTEND

Recommended:

```text
Next.js
TypeScript
Tailwind CSS
```

Alternative:

```text
React
Vite
Tailwind
```

Preferred production choice:

**Next.js + TypeScript + Tailwind CSS**

Structure:

```text
frontend/
├── app/
│   ├── page.tsx
│   ├── about/
│   ├── services/
│   ├── bridal/
│   ├── gallery/
│   ├── booking/
│   ├── contact/
│   └── admin/
├── components/
│   ├── Navbar.tsx
│   ├── Hero.tsx
│   ├── ServiceCard.tsx
│   ├── ServiceGrid.tsx
│   ├── BridalPackages.tsx
│   ├── Gallery.tsx
│   ├── Reviews.tsx
│   ├── BookingForm.tsx
│   ├── Chatbot.tsx
│   └── Footer.tsx
├── lib/
│   └── api.ts
└── public/
    ├── images/
    └── icons/
```

---

# 22. ADMIN DASHBOARD

```text
Dashboard
├── New Leads
├── Appointments
├── Services
├── Prices
├── Gallery
├── Reviews
└── Business Settings
```

Admin capabilities:

- Add/edit/delete service
- Change price
- Change duration
- Enable/disable service
- Upload service image
- View leads
- Update lead status
- View appointments
- Update appointment status
- Manage reviews
- Edit business information
- Edit opening hours

---

# 23. WHATSAPP

Every major CTA should provide WhatsApp.

Example pre-filled message:

```text
Hello Mitalli Bridal World,

I would like to enquire about:

Service:
Preferred Date:
Preferred Time:
```

Do not expose customer phone numbers publicly.

---

# 24. MOBILE CALL BAR

```text
┌──────────┬────────────┬─────────────┐
│   Call   │ WhatsApp   │   Book Now  │
└──────────┴────────────┴─────────────┘
```

Make this prominent on mobile.

---

# 25. SEO

Target keywords:

```text
bridal makeup Sangamner
bridal makeup artist Sangamner
beauty parlour Sangamner
beauty salon Sangamner
bridal makeup near me Sangamner
facial Sangamner
hair spa Sangamner
hydra facial Sangamner
pre bridal makeup Sangamner
```

Metadata:

```text
Title:
Mitalli Bridal World | Bridal Makeup & Beauty Salon in Sangamner

Description:
Professional bridal makeup, skincare, hair care and beauty services at Mitalli Bridal World, Sangamner.
```

Do not claim unconfirmed services.

---

# 26. LOCAL SEO

Implement:

- Google Business Profile link
- Address
- Phone
- Opening hours
- LocalBusiness structured data
- Service structured data where appropriate
- Google Maps
- Consistent NAP information

Keep business name, address and phone consistent across channels.

---

# 27. PERFORMANCE

Target:

```text
Lighthouse Performance: 90+
Mobile-first
Lazy-loaded images
WebP/AVIF images
Compressed assets
Minimal JavaScript
```

---

# 28. SECURITY

Implement:

```text
HTTPS
Environment variables
Password hashing
JWT/session authentication
Input validation
Rate limiting
CORS configuration
SQL injection protection
XSS protection
Admin authentication
```

Never put secrets in frontend code.

Backend environment:

```env
DATABASE_URL=
JWT_SECRET=
ADMIN_EMAIL=
ADMIN_PASSWORD_HASH=
FRONTEND_URL=
WHATSAPP_NUMBER=
```

Frontend:

```env
NEXT_PUBLIC_API_URL=
NEXT_PUBLIC_GOOGLE_MAPS_URL=
```

---

# 29. API ENDPOINTS

## Services

```http
GET /api/services
GET /api/services/{id}
POST /api/services
PUT /api/services/{id}
DELETE /api/services/{id}
```

## Chatbot

```http
POST /api/chat
```

Request:

```json
{
  "message": "Hydra facial कितीला आहे?"
}
```

Response:

```json
{
  "intent": "price_inquiry",
  "reply": "Advanced Hydra Facial ₹3500...",
  "service_id": 3
}
```

## Leads

```http
POST /api/leads
GET /api/leads
PUT /api/leads/{id}
```

## Appointments

```http
POST /api/appointments
GET /api/appointments
PUT /api/appointments/{id}
```

## Reviews

```http
GET /api/reviews
POST /api/reviews
```

---

# 30. CHATBOT FALLBACK

```text
माफ करा 😊 मला तुमचा प्रश्न पूर्णपणे समजला नाही.

तुम्ही खालीलपैकी काही निवडू शकता:

[Services]
[Prices]
[Bridal Makeup]
[Book Appointment]
[Location]
[WhatsApp Us]
```

Never leave the customer at a dead end.

---

# 31. DEVELOPMENT PHASES

## Phase 1 — Foundation

```text
Next.js frontend
FastAPI backend
PostgreSQL
GitHub repository
Environment variables
```

## Phase 2 — Website

```text
Navbar
Hero
About
Services
Bridal Packages
Gallery
Reviews
Contact
Footer
```

## Phase 3 — Database

Create:

```text
services
leads
appointments
reviews
settings
admin_users
```

## Phase 4 — Booking

```text
Booking Form
      ↓
Validation
      ↓
FastAPI
      ↓
PostgreSQL
      ↓
Appointment Request
```

## Phase 5 — Chatbot

```text
Preprocessing
↓
Keyword Detection
↓
Regex
↓
Intent Classification
↓
Database Lookup
↓
Response
```

Start rule-based.

## Phase 6 — Admin Dashboard

```text
Login
Dashboard
Services
Appointments
Leads
Reviews
Settings
```

## Phase 7 — WhatsApp

Add WhatsApp CTA and pre-filled messages.

## Phase 8 — SEO & Deployment

Configure:

```text
Domain
HTTPS
SEO
Sitemap
Robots.txt
Google Search Console
Google Business Profile
Analytics
```

---

# 32. DEPLOYMENT

Recommended low-cost architecture:

```text
                 INTERNET
                    │
                    ▼
             Next.js Website
                    │
                    ▼
             FastAPI Backend
                    │
                    ▼
               PostgreSQL
```

Possible hosting:

```text
Frontend → Vercel
Backend  → Render
Database → PostgreSQL
Images   → Cloudinary / Supabase Storage
```

Verify current free-tier limits before deployment.

---

# 33. GITHUB STRUCTURE

```text
mitalli-bridal-world/
├── frontend/
├── backend/
├── database/
│   ├── schema.sql
│   └── seed.sql
├── docs/
│   ├── API.md
│   ├── DATABASE.md
│   └── DEPLOYMENT.md
├── .gitignore
├── README.md
└── PROJECT_PLAN.md
```

---

# 34. MVP

First production version:

```text
✓ Home
✓ About
✓ Services
✓ Bridal Packages
✓ Gallery
✓ Contact
✓ Call button
✓ WhatsApp button
✓ Booking form
✓ PostgreSQL
✓ Lead collection
✓ Basic chatbot
✓ Admin login
✓ Admin service management
✓ Admin appointment management
```

Do not build advanced AI first.

---

# 35. VERSION 2

```text
✓ Advanced Marathi NLP
✓ Hindi support
✓ Automated email notifications
✓ WhatsApp Business API
✓ Appointment reminders
✓ Customer history
✓ Analytics dashboard
✓ Promotional offers
✓ Coupon system
✓ Blog
```

---

# 36. VERSION 3 — ADVANCED AI

```text
Customer message
       ↓
Intent detection
       ↓
RAG / Knowledge Base
       ↓
LLM
       ↓
Business database
       ↓
Personalized response
```

The AI must only recommend services actually configured in the business database.

---

# 37. DESIGN SYSTEM

Visual direction:

```text
Elegant
Premium
Indian
Bridal
Modern
Trustworthy
Warm
```

Suggested palette:

```text
Primary: Deep Burgundy / Wine
Secondary: Soft Rose
Accent: Muted Gold
Background: Warm Ivory / Cream
Text: Deep Charcoal
```

Do not overuse gold.

Typography:

```text
Heading: Elegant serif
Body: Modern sans-serif
Marathi: Noto Sans Devanagari / Noto Serif Devanagari
```

---

# 38. MOBILE EXPERIENCE

Mobile is the primary experience.

Must have:

```text
Sticky Call
Sticky WhatsApp
Sticky Book Now
Large touch targets
Readable Marathi text
Fast-loading images
Easy forms
```

Booking should be completable with one hand.

---

# 39. CONVERSION STRATEGY

Every major page needs a CTA.

```text
Home      → Book Your Appointment
Services  → Enquire About This Service
Bridal    → Plan Your Bridal Look
Gallery   → Book Your Look
Contact   → Talk to Us on WhatsApp
```

---

# 40. CUSTOMER JOURNEY

```text
Google Search
     ↓
Website
     ↓
Hero
     ↓
Services/Gallery
     ↓
Trust
     ↓
Chatbot
     ↓
Price
     ↓
Booking
     ↓
Lead
     ↓
Staff Confirmation
```

---

# 41. BUSINESS DASHBOARD FLOW

```text
Customer submits inquiry
          ↓
Lead database
          ↓
Admin dashboard
          ↓
Staff contacts customer
          ↓
Appointment confirmed
          ↓
Status = CONFIRMED
```

---

# 42. SUCCESS METRICS

Track:

```text
Website Visitors
Service Page Views
Chatbot Conversations
Price Queries
WhatsApp Clicks
Phone Clicks
Booking Requests
Confirmed Appointments
Lead Conversion Rate
Popular Services
```

Use actual analytics rather than invented figures.

---

# 43. BUSINESS RULES

The chatbot must NOT:

- Invent prices
- Invent availability
- Invent reviews
- Guarantee appointment confirmation
- Claim a disabled/unconfirmed service exists
- Give medical advice
- Promise specific treatment results

Use:

> Your appointment request has been received. Our team will confirm the slot.

rather than:

> Your appointment is confirmed.

unless actual availability has been checked.

---

# 44. DATA PRIVACY

Customer data:

```text
Name
Phone
Appointment
Service
Message
```

Use only for appointment handling, customer communication and business operations.

Add a simple privacy notice to the booking form.

---

# 45. FINAL TECH STACK

### Frontend

```text
Next.js
TypeScript
Tailwind CSS
```

### Backend

```text
Python
FastAPI
Pydantic
SQLAlchemy
```

### Database

```text
PostgreSQL
```

### Chatbot

```text
Python
Regex
NLTK / lightweight NLP
Database lookup
```

### Storage

```text
Supabase Storage / Cloudinary
```

### Hosting

```text
Vercel
+
Render
+
PostgreSQL
```

### Version Control

```text
GitHub
```

---

# 46. FINAL ARCHITECTURE

```text
                         CUSTOMER
                            │
                            ▼
                  ┌──────────────────┐
                  │  MITALLI WEBSITE │
                  └────────┬─────────┘
                           │
            ┌──────────────┼───────────────┐
            │              │               │
            ▼              ▼               ▼
        Services       Gallery         Chatbot
            │              │               │
            │              │               ▼
            │              │         FastAPI NLP
            │              │               │
            │              │               ▼
            │              │         PostgreSQL
            │              │               │
            └──────────────┼───────────────┘
                           │
                           ▼
                    Booking / Lead
                           │
                           ▼
                    ADMIN DASHBOARD
                           │
              ┌────────────┼─────────────┐
              ▼            ▼             ▼
            Leads     Appointments    Services
              │            │             │
              └────────────┼─────────────┘
                           ▼
                    OWNER / STAFF
```

---

# 47. DEVELOPMENT PRIORITY

Build in this exact order:

```text
1. Database
2. FastAPI
3. Services API
4. Frontend layout
5. Home page
6. Services page
7. Gallery
8. Booking form
9. Lead system
10. Admin authentication
11. Admin dashboard
12. Chatbot
13. WhatsApp integration
14. SEO
15. Deployment
16. Analytics
```

---

# 48. DEFINITION OF DONE

```text
[✓] Website works on mobile
[✓] Website works on desktop
[✓] Services load from database
[✓] Prices load dynamically
[✓] Admin can change prices
[✓] Customer can submit booking request
[✓] Booking enters PostgreSQL
[✓] Lead enters PostgreSQL
[✓] Admin can view leads
[✓] Admin can view appointments
[✓] Admin can change appointment status
[✓] Chatbot answers common questions
[✓] Chatbot supports Marathi/English
[✓] WhatsApp CTA works
[✓] Call CTA works
[✓] Location information works
[✓] Gallery works
[✓] SEO metadata configured
[✓] HTTPS enabled
[✓] Secrets stored securely
[✓] No fake reviews
[✓] No unverified business claims
```

---

# 49. CORE PRODUCT VISION

The product should not be positioned simply as:

> "A website for a beauty parlour."

Instead:

> **A complete digital customer acquisition and appointment system for Mitalli Bridal World.**

Workflow:

```text
Search
 ↓
Website
 ↓
Information
 ↓
Chat
 ↓
Lead
 ↓
Appointment
 ↓
Customer
```

---

# 50. FIRST MVP DELIVERABLE

```text
MITALLI BRIDAL WORLD

        HOME
          │
   ┌──────┼────────┐
   │      │        │
Services Bridal  Gallery
   │      │        │
   └──────┼────────┘
          │
      BOOK NOW
          │
       Booking
          │
      PostgreSQL
          │
     Admin Panel
          │
       Leads
          │
      Follow-up
```

Then add the intelligent Marathi/English chatbot after the core booking and lead pipeline works.

---

# 51. PRIMARY DEVELOPMENT PRINCIPLE

**Database first → API second → UI third → chatbot fourth → automation fifth.**

Do not build the chatbot before the underlying service, pricing, lead and appointment database exists.

This ensures the chatbot becomes an interface to the actual business system rather than a hard-coded demo.
