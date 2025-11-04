from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.schemas.job import CreateJob, UpdateJob
from app.services.job import (
    create_job_service,
    get_all_jobs,
    update_job,
    delete_job_service,
)

job_router = APIRouter(prefix="/jobs", tags=["jobs"])


# Create
@job_router.post("/createjob")
def create_job(job: CreateJob, db: Session = Depends(get_db)):
    return create_job_service(job, db)


# Read
@job_router.get("/alljobs")
def get_jobs(db: Session = Depends(get_db)):
    return get_all_jobs(db)


# Update
@job_router.put("/updatejob/{job_id}")
def update_job(job_id: int, updated_job: UpdateJob, db: Session = Depends(get_db)):
    return update_job(job_id, updated_job, db)


@job_router.delete("/deletejob/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    return delete_job_service(job_id, db)
