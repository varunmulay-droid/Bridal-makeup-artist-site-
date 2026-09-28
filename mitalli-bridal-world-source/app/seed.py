import os
from .database import SessionLocal, engine, Base
from . import models
from .auth import hash_password
from .config import ALL_DEFAULT_SETTINGS, CONFIRMED_KEYS

SERVICES = [
    # category, name, description, duration, price, price_type
    ("Bridal Makeup", "Classic Bridal Makeup", "Elegant, professional bridal makeup finish.", 90, 12000, "starting_from"),
    ("Bridal Makeup", "HD Bridal Makeup", "High-definition makeup for a flawless camera-ready look.", 120, 18000, "starting_from"),
    ("Bridal Makeup", "Airbrush Bridal Makeup", "Long-lasting airbrush application for premium finish.", 120, 18000, "starting_from"),
    ("Facial & Skincare", "Cleanup", "Quick refresh cleanup for glowing skin.", 30, 500, "fixed"),
    ("Facial & Skincare", "Fruit Facial", "Natural fruit-based facial treatment.", 45, 1200, "fixed"),
    ("Facial & Skincare", "Gold Facial", "Radiance-boosting gold facial.", 45, 1200, "fixed"),
    ("Facial & Skincare", "Hydra Facial", "Deep hydration advanced facial treatment.", 60, 3500, "starting_from"),
    ("Hair Care", "Hair Spa", "Nourishing hair spa treatment.", 45, 999, "starting_from"),
    ("Hair Care", "Hair Smoothening / Keratin", "Smooth, frizz-free, manageable hair.", 120, 4500, "starting_from"),
    ("Hair Care", "Hair Styling", "Professional styling for any occasion.", 45, None, "on_request"),
    ("Hair Care", "Hair Extensions", "Length and volume extensions.", 90, None, "on_request"),
    ("Hair Care", "Hair Straightening", "Salon-grade straightening treatment.", 90, None, "on_request"),
    ("Nails", "Manicure", "Classic manicure.", 30, None, "on_request"),
    ("Nails", "Pedicure", "Relaxing pedicure treatment.", 45, None, "on_request"),
    ("Nails", "Nail Extensions", "Artificial nail extensions.", 60, None, "on_request"),
    ("Nails", "Nail Art", "Custom nail art design.", 30, None, "on_request"),
    ("Waxing & Threading", "Waxing + Threading Package", "Full body waxing and threading combo.", 60, 800, "starting_from"),
    ("Other Services", "Saree Draping", "Professional saree draping for events.", 30, None, "on_request"),
    ("Other Services", "Event Makeup", "Makeup for festive and special occasions.", 60, None, "on_request"),
]

BRIDAL_PACKAGES = [
    ("Classic Bridal", 12000, "starting_from",
     "Bridal Makeup\nProfessional Finish\nPersonalized Look", 0),
    ("HD / Airbrush Premium", 18000, "starting_from",
     "HD/Airbrush Makeup\nPremium Bridal Finish\nPersonalized Styling", 1),
]


def run():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        # Settings
        for key, value in ALL_DEFAULT_SETTINGS.items():
            existing = db.query(models.SiteSetting).filter(models.SiteSetting.key == key).first()
            if not existing:
                db.add(models.SiteSetting(
                    key=key, value=value, is_confirmed=(key in CONFIRMED_KEYS)
                ))

        # Services
        if db.query(models.Service).count() == 0:
            for category, name, desc, duration, price, price_type in SERVICES:
                db.add(models.Service(
                    category=category, name=name, description=desc,
                    duration_minutes=duration, price=price, price_type=price_type,
                    is_active=True,
                ))

        # Bridal packages (NOT published by default — owner must confirm inclusions/price first)
        if db.query(models.BridalPackage).count() == 0:
            for name, price, price_type, inclusions, order in BRIDAL_PACKAGES:
                db.add(models.BridalPackage(
                    name=name, price=price, price_type=price_type,
                    inclusions=inclusions, is_published=False, display_order=order,
                ))

        # Admin user
        if db.query(models.AdminUser).count() == 0:
            admin_username = os.getenv("ADMIN_USERNAME", "admin")
            admin_password = os.getenv("ADMIN_PASSWORD", "ChangeMe123!")
            db.add(models.AdminUser(
                username=admin_username,
                hashed_password=hash_password(admin_password),
            ))
            print(f"Created admin user '{admin_username}'. "
                  f"{'Using ADMIN_PASSWORD env var.' if os.getenv('ADMIN_PASSWORD') else 'DEFAULT PASSWORD IS ChangeMe123! — CHANGE IT.'}")

        db.commit()
        print("Seed complete.")
    finally:
        db.close()


if __name__ == "__main__":
    run()
