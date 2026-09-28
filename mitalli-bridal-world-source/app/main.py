import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from .database import Base, engine
from .routers import public, booking, admin
from . import seed

app = FastAPI(title="Mitalli Bridal World & Makeover Studio")

# Sessions (used for simple admin login). Set SECRET_KEY as a Render env var in production.
app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY", "dev-secret-change-me"),
    https_only=os.getenv("ENV", "development") == "production",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(public.router)
app.include_router(booking.router)
app.include_router(admin.router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    # Idempotent seed: only inserts rows that don't already exist.
    seed.run()


@app.get("/health")
def health():
    return {"status": "ok"}
