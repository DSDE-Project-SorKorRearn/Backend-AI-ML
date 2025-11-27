from sqlalchemy import Column, DateTime, Float, Integer, String, Text

from .database import Base


class Traffy(Base):
    __tablename__ = "traffy"

    index = Column(Integer, primary_key=True, index=True)
    traffy_type = Column(String, index=True)  # Maps to 'type'
    organization = Column(String)
    detail = Column(Text)  # Maps to 'comment'
    photo = Column(String)
    photo_after = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    address = Column(Text)
    subdistrict = Column(String)
    district = Column(String, index=True)
    province = Column(String, index=True)
    timestamp = Column(DateTime, index=True)  # Maps to 'timestamp'
    state = Column(String)
    star = Column(Float)
    count_reopen = Column(Integer)
    last_activity = Column(DateTime)
