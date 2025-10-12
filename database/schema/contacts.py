from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Contacts(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    address = Column(String)
    job_id =Column(Integer, ForeignKey('jobs.id'))