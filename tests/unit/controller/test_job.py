from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestJob:
    def test_create_job(self, mocker):
        payload = {
            "title": "Software Engineer",
            "company": "Tech Corp",
            "location": "New York",
            "status": "Applied",
            "applied_date": "2023-10-01.",
        }
        new_job = {
            "id": 1,
            "title": "Software Engineer",
            "company": "Tech Corp",
            "location": "New York",
            "status": "Applied",
            "applied_date": "2023-10-01.",
        }
        job_creation_result = {"message": "Job Created successfully", "job": new_job}
        mock_job_creation_service = mocker.patch(
            "app.api.jobs.create_job_service", return_value=job_creation_result
        )

        response = client.post("/jobs/createjob", json=payload)
        assert response.status_code == 200
        assert response.json() == job_creation_result
        mock_job_creation_service.assert_called()
