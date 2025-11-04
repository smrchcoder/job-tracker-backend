from sqlalchemy import Column, Date, Integer, String
from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    skills = Column(String, nullable=True)
    currentCompany = Column(String, nullable=True)
    experience = Column(Integer, nullable=True)
    phone = Column(Integer, unique=True, nullable=True)
    dob = Column(Date, nullable=True)
