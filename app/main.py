from fastapi import FastAPI
from app.api.router import api_router
from app.db.session import engine, Base
from app.models import user  # registers the User model

app = FastAPI(title="Course Enrollment Platform")
app.include_router(api_router)

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}