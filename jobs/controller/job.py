from fastapi import APIRouter, Depends
from ..model import CreateJob, UpdateJob
from ..service import job as job_service
from database import get_db
from sqlalchemy.orm import Session
job_router = APIRouter(prefix='/jobs', tags=['jobs'])


# Create
@job_router.post('/createjob')
def create_job(job: CreateJob, db: Session = Depends(get_db)):
    return job_service.create_job_service(job, db)

# Read
@job_router.get('/alljobs')
def get_jobs(db: Session = Depends(get_db)):
    return job_service.get_all_jobs(db)

# Update
@job_router.put('/updatejob/{job_id}')
def update_job(job_id: int, updated_job: UpdateJob, db: Session = Depends(get_db)):
    return job_service.update_job(job_id, updated_job, db)

# Delete