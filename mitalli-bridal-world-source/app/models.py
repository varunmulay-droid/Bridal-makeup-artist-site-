from datetime import datetime
from sqlalchemy import (
    Column, Integer, String, Text, Boolean, DateTime, Date, Time,
    ForeignKey, CheckConstraint
)
from sqlalchemy.orm import relationship
from .database import Base


class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(100), nullable=False, index=True)
    name = Column(String(150), nullable=False)
    description = Column(Text, default="")
    duration_minutes = Column(Integer, nullable=True)
    price = Column(Integer, nullable=True)  # in INR, nullable for "on request"
    price_type = Column(String(30), default="fixed")  # fixed | starting_from | custom | on_request
    image_url = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    appointments = relationship("Appointment", back_populates="service")


class BridalPackage(Base):
    __tablename__ = "bridal_packages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    price = Column(Integer, nullable=True)
    price_type = Column(String(30), default="starting_from")
    inclusions = Column(Text, default="")  # newline-separated bullet points
    is_published = Column(Boolean, default=False)  # owner must confirm before going live
    display_order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(150), nullable=False)
    phone = Column(String(20), nullable=False)
    service_id = Column(Integer, ForeignKey("services.id"), nullable=True)
    appointment_date = Column(Date, nullable=True)
    preferred_time = Column(Time, nullable=True)
    message = Column(Text, nullable=True)
    status = Column(String(30), default="pending")  # pending, contacted, confirmed, completed, cancelled
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    service = relationship("Service", back_populates="appointments")

    __table_args__ = (
        CheckConstraint(
            status.in_(["pending", "contacted", "confirmed", "completed", "cancelled"]),
            name="ck_appointment_status",
        ),
    )


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=True)
    phone = Column(String(20), nullable=True)
    source = Column(String(50), default="website")  # website, chatbot, whatsapp, call
    service_interest = Column(String(150), nullable=True)
    message = Column(Text, nullable=True)
    status = Column(String(30), default="new")  # new, contacted, converted, closed
    created_at = Column(DateTime, default=datetime.utcnow)


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(150))
    rating = Column(Integer)
    review_text = Column(Text)
    service = Column(String(150), nullable=True)
    is_featured = Column(Boolean, default=False)
    is_approved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        CheckConstraint("rating BETWEEN 1 AND 5", name="ck_review_rating"),
    )


class SiteSetting(Base):
    """Key/value store so the owner can edit business facts (hours, phone, rating, etc.)
    from the admin panel without touching code — see Section 2 of the project plan."""
    __tablename__ = "site_settings"

    key = Column(String(100), primary_key=True)
    value = Column(Text, nullable=True)
    is_confirmed = Column(Boolean, default=False)  # owner has verified this value
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class AdminUser(Base):
    __tablename__ = "admin_users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
