from database import Base
from sqlalchemy import Column, Date , Integer , String
class User(Base):
    __tablename__ = 'users' 

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)  # Not optional
    email = Column(String, unique=True, nullable=False)  # Not optional
    hashed_password = Column(String, nullable=False)  # Not optional
    skills = Column(String, nullable=True)  # Optional
    currentCompany = Column(String, nullable=True)  # Optional
    experience = Column(Integer, nullable=True)  # Optional
    phone = Column(Integer, unique=True, nullable=True)  # Optional
    dob = Column(Date, nullable=True)  # Optional