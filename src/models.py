from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text
from datetime import datetime
from database import Base


class CameraModel(Base):
    __tablename__ = 'cameras'
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, nullable=False)
    brand = Column(String, nullable=False)



    
