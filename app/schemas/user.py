from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import date


class UserCreate(BaseModel):
    username: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    password: str
    dob: date = None
    phone: int = None
    currentCompany: str = None
    experience: int = None
    skills: list[str] = None

    @field_validator("phone")
    def validate_phone(cls, v):
        if v is not None and (v < 1000000000 or v > 9999999999):
            raise ValueError("Phone number must be a 10-digit integer")
        return v


class UserLogin(BaseModel):
    email: EmailStr
    password: str
