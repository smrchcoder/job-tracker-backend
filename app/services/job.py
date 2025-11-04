from sqlalchemy.orm import Session
from app.schemas.job import CreateJob, UpdateJob
from app.models.job import Job


def create_job_service(new_job: CreateJob, db: Session):
    # Logic to create a job in the database
    job = db.query(Job).filter(Job.company == new_job.company).first()
    if job and job.title == new_job.title:
        return {"message": "Job already exists"}
    new_job_instance = Job(**new_job.model_dump())
    try:
        db.add(new_job_instance)
        db.commit()
        db.refresh(new_job_instance)
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        return {"message": "Failed to create job"}
    return {"message": "Job created successfully", "job": new_job_instance}


def get_all_jobs(db: Session):
    jobs = db.query(Job).all()
    try:
        return {"jobs": jobs}
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"message": "Failed to fetch jobs"}


def update_job(job_id: int, updated_job: UpdateJob, db: Session):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        return {"message": "Job not found"}
    for key, value in updated_job.model_dump().items():
        if value is not None:
            setattr(job, key, value)
    try:
        db.commit()
        db.refresh(job)
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        return {"message": "Failed to update job"}
    return {"message": "Job updated successfully", "job": job}


def delete_job_service(job_id: int, db: Session):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        return {"message": "Job not found"}
    try:
        db.delete(job)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        return {"message": "Failed to delete job"}
    return {"message": "Job deleted successfully"}
