from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from app.api.auth import auth_router
from app.api.jobs import job_router

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Job Application Tracker API", version="1.0.0")

# Include routers
app.include_router(auth_router)
app.include_router(job_router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allows  requests from any origin
    allow_credentials=True,  # allows cookies, authorization headers, etc.
    allow_methods=["*"],  # allows all HTTP methods
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Application Tracker API"}
