from sqlalchemy import Column, Integer, String, JSON

from app.db import Base


class Hotel(Base):
    __tablename__ = 'hotel'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False, index=True)
    services = Column(JSON)
    room_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)
