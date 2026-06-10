from fastapi import FastAPI
from app.api.router import api_router

app = FastAPI(title="Course Enrollment Platform")
app.include_router(api_router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
