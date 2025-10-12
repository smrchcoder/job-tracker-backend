from database import Base
from sqlalchemy import Column, Integer , String, ForeignKey

class Job(Base):
    __tablename__ = 'jobs'

    id =Column(Integer , primary_key=True, index=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    status = Column(String)
    applied_date = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    
    
