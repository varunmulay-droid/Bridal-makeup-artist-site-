from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


def get_settings_dict(db: Session):
    rows = db.query(models.SiteSetting).all()
    return {r.key: r.value for r in rows}


@router.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    settings = get_settings_dict(db)
    featured_services = (
        db.query(models.Service)
        .filter(models.Service.is_active.is_(True))
        .limit(6)
        .all()
    )
    packages = (
        db.query(models.BridalPackage)
        .filter(models.BridalPackage.is_published.is_(True))
        .order_by(models.BridalPackage.display_order)
        .all()
    )
    reviews = (
        db.query(models.Review)
        .filter(models.Review.is_approved.is_(True), models.Review.is_featured.is_(True))
        .limit(3)
        .all()
    )
    return templates.TemplateResponse("home.html", {
        "request": request, "settings": settings,
        "featured_services": featured_services, "packages": packages, "reviews": reviews,
    })


@router.get("/about")
def about(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("about.html", {
        "request": request, "settings": get_settings_dict(db),
    })


@router.get("/services")
def services(request: Request, db: Session = Depends(get_db)):
    all_services = (
        db.query(models.Service)
        .filter(models.Service.is_active.is_(True))
        .order_by(models.Service.category, models.Service.name)
        .all()
    )
    by_category = {}
    for s in all_services:
        by_category.setdefault(s.category, []).append(s)
    return templates.TemplateResponse("services.html", {
        "request": request, "settings": get_settings_dict(db), "by_category": by_category,
    })


@router.get("/bridal-packages")
def bridal_packages(request: Request, db: Session = Depends(get_db)):
    packages = (
        db.query(models.BridalPackage)
        .filter(models.BridalPackage.is_published.is_(True))
        .order_by(models.BridalPackage.display_order)
        .all()
    )
    return templates.TemplateResponse("bridal.html", {
        "request": request, "settings": get_settings_dict(db), "packages": packages,
    })


@router.get("/gallery")
def gallery(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("gallery.html", {
        "request": request, "settings": get_settings_dict(db),
    })


@router.get("/reviews")
def reviews(request: Request, db: Session = Depends(get_db)):
    approved_reviews = (
        db.query(models.Review)
        .filter(models.Review.is_approved.is_(True))
        .order_by(models.Review.created_at.desc())
        .all()
    )
    return templates.TemplateResponse("reviews.html", {
        "request": request, "settings": get_settings_dict(db), "reviews": approved_reviews,
    })


@router.get("/contact")
def contact(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("contact.html", {
        "request": request, "settings": get_settings_dict(db),
    })
