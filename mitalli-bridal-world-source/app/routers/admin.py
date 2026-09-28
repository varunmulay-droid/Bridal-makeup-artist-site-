from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models
from ..auth import verify_password

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="app/templates")


def _require_admin(request: Request):
    if not request.session.get("admin_user"):
        return RedirectResponse(url="/admin/login", status_code=303)
    return None


@router.get("/login")
def login_page(request: Request):
    if request.session.get("admin_user"):
        return RedirectResponse(url="/admin", status_code=303)
    return templates.TemplateResponse("admin/login.html", {"request": request, "error": None})


@router.post("/login")
def login_submit(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(models.AdminUser).filter(models.AdminUser.username == username).first()
    if not user or not verify_password(password, user.hashed_password):
        return templates.TemplateResponse("admin/login.html", {
            "request": request, "error": "Invalid username or password.",
        })
    request.session["admin_user"] = username
    return RedirectResponse(url="/admin", status_code=303)


@router.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/admin/login", status_code=303)


@router.get("")
def dashboard(request: Request, db: Session = Depends(get_db)):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    stats = {
        "leads_new": db.query(models.Lead).filter(models.Lead.status == "new").count(),
        "appointments_pending": db.query(models.Appointment).filter(models.Appointment.status == "pending").count(),
        "services_active": db.query(models.Service).filter(models.Service.is_active.is_(True)).count(),
        "unconfirmed_settings": db.query(models.SiteSetting).filter(models.SiteSetting.is_confirmed.is_(False)).count(),
    }
    return templates.TemplateResponse("admin/dashboard.html", {
        "request": request, "stats": stats, "admin_user": request.session.get("admin_user"),
    })


# ---------- Services ----------

@router.get("/services")
def admin_services(request: Request, db: Session = Depends(get_db)):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    services = db.query(models.Service).order_by(models.Service.category, models.Service.name).all()
    return templates.TemplateResponse("admin/services.html", {"request": request, "services": services})


@router.post("/services/{service_id}/update")
def update_service(
    request: Request, service_id: int, db: Session = Depends(get_db),
    price: str = Form(None), price_type: str = Form("fixed"), is_active: str = Form(None),
):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    service = db.query(models.Service).filter(models.Service.id == service_id).first()
    if not service:
        raise HTTPException(404)
    service.price = int(price) if price else None
    service.price_type = price_type
    service.is_active = bool(is_active)
    db.commit()
    return RedirectResponse(url="/admin/services", status_code=303)


# ---------- Bridal packages ----------

@router.get("/packages")
def admin_packages(request: Request, db: Session = Depends(get_db)):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    packages = db.query(models.BridalPackage).order_by(models.BridalPackage.display_order).all()
    return templates.TemplateResponse("admin/packages.html", {"request": request, "packages": packages})


@router.post("/packages/{package_id}/update")
def update_package(
    request: Request, package_id: int, db: Session = Depends(get_db),
    price: str = Form(None), inclusions: str = Form(""), is_published: str = Form(None),
):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    pkg = db.query(models.BridalPackage).filter(models.BridalPackage.id == package_id).first()
    if not pkg:
        raise HTTPException(404)
    pkg.price = int(price) if price else None
    pkg.inclusions = inclusions
    pkg.is_published = bool(is_published)
    db.commit()
    return RedirectResponse(url="/admin/packages", status_code=303)


# ---------- Appointments ----------

@router.get("/appointments")
def admin_appointments(request: Request, db: Session = Depends(get_db)):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    appointments = db.query(models.Appointment).order_by(models.Appointment.created_at.desc()).all()
    return templates.TemplateResponse("admin/appointments.html", {"request": request, "appointments": appointments})


@router.post("/appointments/{appointment_id}/status")
def update_appointment_status(request: Request, appointment_id: int, status: str = Form(...), db: Session = Depends(get_db)):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    appt = db.query(models.Appointment).filter(models.Appointment.id == appointment_id).first()
    if not appt:
        raise HTTPException(404)
    if status not in ["pending", "contacted", "confirmed", "completed", "cancelled"]:
        raise HTTPException(400, "Invalid status")
    appt.status = status
    db.commit()
    return RedirectResponse(url="/admin/appointments", status_code=303)


# ---------- Leads ----------

@router.get("/leads")
def admin_leads(request: Request, db: Session = Depends(get_db)):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    leads = db.query(models.Lead).order_by(models.Lead.created_at.desc()).all()
    return templates.TemplateResponse("admin/leads.html", {"request": request, "leads": leads})


@router.post("/leads/{lead_id}/status")
def update_lead_status(request: Request, lead_id: int, status: str = Form(...), db: Session = Depends(get_db)):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    lead = db.query(models.Lead).filter(models.Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(404)
    if status not in ["new", "contacted", "converted", "closed"]:
        raise HTTPException(400, "Invalid status")
    lead.status = status
    db.commit()
    return RedirectResponse(url="/admin/leads", status_code=303)


# ---------- Site settings ----------

@router.get("/settings")
def admin_settings(request: Request, db: Session = Depends(get_db)):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    settings = db.query(models.SiteSetting).order_by(models.SiteSetting.key).all()
    return templates.TemplateResponse("admin/settings.html", {"request": request, "settings": settings})


@router.post("/settings/{key}/update")
def update_setting(request: Request, key: str, value: str = Form(""), is_confirmed: str = Form(None), db: Session = Depends(get_db)):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    setting = db.query(models.SiteSetting).filter(models.SiteSetting.key == key).first()
    if not setting:
        raise HTTPException(404)
    setting.value = value
    setting.is_confirmed = bool(is_confirmed)
    db.commit()
    return RedirectResponse(url="/admin/settings", status_code=303)


# ---------- Reviews ----------

@router.get("/reviews")
def admin_reviews(request: Request, db: Session = Depends(get_db)):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    reviews = db.query(models.Review).order_by(models.Review.created_at.desc()).all()
    return templates.TemplateResponse("admin/reviews.html", {"request": request, "reviews": reviews})


@router.post("/reviews/{review_id}/approve")
def approve_review(request: Request, review_id: int, is_approved: str = Form(None), is_featured: str = Form(None), db: Session = Depends(get_db)):
    redirect = _require_admin(request)
    if redirect:
        return redirect
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if not review:
        raise HTTPException(404)
    review.is_approved = bool(is_approved)
    review.is_featured = bool(is_featured)
    db.commit()
    return RedirectResponse(url="/admin/reviews", status_code=303)
