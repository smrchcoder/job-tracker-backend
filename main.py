from fastapi import FastAPI
from jobs.controller.job import job_router
from fastapi.middleware.cors import CORSMiddleware
from auth.authcontroller import auth_router 
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()
app.include_router(job_router)
app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create database tables
@app.get("/")
def read_root():
    return {"message": "Welcome to the Job Application Tracker API"}
