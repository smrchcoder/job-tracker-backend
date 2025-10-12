from pydantic import BaseModel, Field
from typing import Optional

class CreateJob(BaseModel):
    title: str = Field(..., example="Software Engineer")
    company: str = Field(..., example='OpenAI')
    location: str = Field(..., example="San Francisco, CA")
    status: str = Field(..., example="Applied")
    applied_date: str = Field(..., example="2023-10-01")

class UpdateJob(BaseModel):
    title: Optional[str] = Field(None, example="Software Engineer")
    company: Optional[str] = Field(None, example='OpenAI')
    location: Optional[str] = Field(None, example="San Francisco, CA")
    status: Optional[str] = Field(None, example="Applied")
    applied_date: Optional[str] = Field(None, example="2023-10-01")
