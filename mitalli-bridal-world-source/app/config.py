"""
Business info defaults.

Per the project plan's data policy: VERIFIED values come from the public
Justdial listing. OWNER-CONFIRMATION values must be checked with the salon
owner before being trusted/publicized — they are seeded into site_settings
with is_confirmed=False so the admin panel visibly flags them until an
admin edits and confirms them.
"""

BUSINESS_NAME = "Mitalli Bridal World & Makeover Studio"

VERIFIED_SETTINGS = {
    "established_year": "2006",
    "address_line": "Near Mantri Bank, Nashik Road, Sangamner, Maharashtra 422605",
    "phone": "07383099084",
    "hours": "Monday–Saturday: 9:30 AM – 6:30 PM | Sunday: Closed",
    "justdial_rating": "3.8/5 (4 ratings)",
    "justdial_url": "https://www.justdial.com/Sangamner/Mitalli-Bridal-World-Near-Mantri-Bank-Sangamner/9999PX241-X241-150312182233-A6B6_BZDET",
}

# These are seeded but marked unconfirmed — shown in admin with a "confirm with owner" flag.
UNCONFIRMED_SETTINGS = {
    "alt_rating": "4.7/5",
    "avg_response_time": "35+ minutes",
    "alt_hours": "10:00 AM – 8:00 PM",
    "whatsapp_number": "",  # fill in once confirmed
    "google_maps_embed_url": "",  # exact map pin pending owner confirmation
}

ALL_DEFAULT_SETTINGS = {**VERIFIED_SETTINGS, **UNCONFIRMED_SETTINGS}
CONFIRMED_KEYS = set(VERIFIED_SETTINGS.keys())
