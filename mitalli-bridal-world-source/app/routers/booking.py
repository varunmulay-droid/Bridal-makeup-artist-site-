from datetime import datetime
from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from pydantic import BaseModel

from ..database import get_db
from .. import models
from ..chatbot import get_reply
from .public import get_settings_dict

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/booking")
def booking_form(request: Request, db: Session = Depends(get_db)):
    active_services = (
        db.query(models.Service)
        .filter(models.Service.is_active.is_(True))
        .order_by(models.Service.category, models.Service.name)
        .all()
    )
    return templates.TemplateResponse("booking.html", {
        "request": request, "settings": get_settings_dict(db), "services": active_services,
    })


@router.post("/booking")
def submit_booking(
    request: Request,
    db: Session = Depends(get_db),
    customer_name: str = Form(...),
    phone: str = Form(...),
    service_id: int = Form(None),
    appointment_date: str = Form(None),
    preferred_time: str = Form(None),
    message: str = Form(None),
):
    appt = models.Appointment(
        customer_name=customer_name.strip(),
        phone=phone.strip(),
        service_id=service_id if service_id else None,
        appointment_date=datetime.strptime(appointment_date, "%Y-%m-%d").date() if appointment_date else None,
        preferred_time=datetime.strptime(preferred_time, "%H:%M").time() if preferred_time else None,
        message=message,
        status="pending",
    )
    db.add(appt)

    # Every appointment request also becomes a lead (Section 16 of the plan)
    service_name = None
    if service_id:
        svc = db.query(models.Service).filter(models.Service.id == service_id).first()
        service_name = svc.name if svc else None
    db.add(models.Lead(
        name=customer_name.strip(), phone=phone.strip(), source="website",
        service_interest=service_name, message=message, status="new",
    ))
    db.commit()

    return templates.TemplateResponse("booking_success.html", {
        "request": request, "settings": get_settings_dict(db),
    })


@router.post("/contact")
def submit_contact_lead(
    request: Request,
    db: Session = Depends(get_db),
    name: str = Form(...),
    phone: str = Form(...),
    message: str = Form(None),
):
    db.add(models.Lead(
        name=name.strip(), phone=phone.strip(), source="website",
        message=message, status="new",
    ))
    db.commit()
    return templates.TemplateResponse("contact_success.html", {
        "request": request, "settings": get_settings_dict(db),
    })


class ChatMessage(BaseModel):
    message: str


@router.post("/api/chat")
def chat(payload: ChatMessage, db: Session = Depends(get_db)):
    reply = get_reply(db, payload.message)
    # Log chatbot interactions as leads only when they look like genuine enquiries
    # (kept minimal for MVP — full conversation logging is a Version 2 item).
    return {"reply": reply}
