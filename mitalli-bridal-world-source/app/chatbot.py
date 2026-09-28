"""
Lightweight rule-based chatbot (Section 36 says advanced NLP/RAG is Version 3 —
this is the intentional MVP version: keyword matching against the live database,
never inventing prices, availability, or reviews).
"""
import re
from sqlalchemy.orm import Session
from . import models

GREETING_WORDS = {"hi", "hello", "hey", "namaste", "नमस्ते", "namaskar", "नमस्कार"}

PRICE_WORDS = {"price", "cost", "rate", "charges", "किंमत", "दर", "भाव"}
HOURS_WORDS = {"hours", "timing", "time", "open", "close", "वेळ", "टाइम"}
LOCATION_WORDS = {"location", "address", "where", "पत्ता", "कुठे", "लोकेशन"}
BRIDAL_WORDS = {"bridal", "bride", "wedding", "लग्न", "नवरी", "ब्राईडल"}
BOOKING_WORDS = {"book", "appointment", "booking", "बुक", "अपॉइंटमेंट"}
CONTACT_WORDS = {"phone", "call", "whatsapp", "contact", "नंबर", "फोन"}


def _get_setting(db: Session, key: str, default: str = "") -> str:
    row = db.query(models.SiteSetting).filter(models.SiteSetting.key == key).first()
    return row.value if row and row.value else default


def _tokenize(text: str):
    return set(re.findall(r"[\w\u0900-\u097F]+", text.lower()))


def get_reply(db: Session, message: str) -> str:
    tokens = _tokenize(message)

    if tokens & GREETING_WORDS:
        return (
            "Namaste! Welcome to Mitalli Bridal World 🌸 I can help with services, "
            "pricing, bridal packages, timings, location, or booking an appointment. "
            "What would you like to know? / नमस्कार! मी सेवा, किंमत, वेळ, पत्ता किंवा "
            "अपॉइंटमेंट बुकिंगबद्दल मदत करू शकते."
        )

    if tokens & BOOKING_WORDS:
        return (
            "You can request an appointment using the Booking form on this site, or "
            "tap the WhatsApp/Call button for a quicker response. Please note: submitting "
            "a request does not guarantee the slot — our team will confirm it with you."
        )

    if tokens & HOURS_WORDS:
        hours = _get_setting(db, "hours", "Please contact us for current timings.")
        return f"Our listed hours are: {hours}. Please call to confirm for holidays/festivals."

    if tokens & LOCATION_WORDS:
        address = _get_setting(db, "address_line", "Sangamner, Maharashtra")
        return f"We're located at: {address}. Tap 'Get Directions' on the Contact page for a map."

    if tokens & CONTACT_WORDS:
        phone = _get_setting(db, "phone", "")
        whatsapp = _get_setting(db, "whatsapp_number", "")
        parts = []
        if phone:
            parts.append(f"Call us at {phone}")
        if whatsapp:
            parts.append(f"WhatsApp us at {whatsapp}")
        return " or ".join(parts) if parts else "Please use the Call or WhatsApp button on this site."

    if tokens & BRIDAL_WORDS:
        packages = (
            db.query(models.BridalPackage)
            .filter(models.BridalPackage.is_published.is_(True))
            .order_by(models.BridalPackage.display_order)
            .all()
        )
        if not packages:
            return (
                "We offer bridal makeup packages — final pricing and inclusions are being "
                "confirmed with our team. Please enquire directly for the latest bridal details!"
            )
        lines = []
        for p in packages:
            price_str = f"starting at ₹{p.price:,}" if p.price else "on request"
            lines.append(f"• {p.name} — {price_str}")
        return "Here are our bridal packages:\n" + "\n".join(lines) + \
            "\nWould you like to enquire about one of these?"

    if tokens & PRICE_WORDS:
        services = (
            db.query(models.Service)
            .filter(models.Service.is_active.is_(True), models.Service.price.isnot(None))
            .limit(8)
            .all()
        )
        if not services:
            return "Please share which service you're asking about, and I'll check the current price."
        lines = [f"• {s.name}: ₹{s.price:,}" for s in services]
        return "Here are some of our current prices:\n" + "\n".join(lines) + \
            "\nPrices may vary by requirement — let us know your exact need for an accurate quote."

    return (
        "I can help with services, pricing, bridal packages, hours, location, or booking. "
        "Could you tell me a bit more about what you're looking for? / कृपया अधिक माहिती द्या."
    )
