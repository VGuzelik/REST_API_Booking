from sqlalchemy import (JSON, CheckConstraint, Column, ForeignKey, Integer,
                        String)

from app.db import Base


class Room(Base):
    __tablename__ = 'room'


    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey('hotel.id', ondelete='cascade'))
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)
    services = Column(JSON)
    quantity = Column(Integer, nullable=False)
    CheckConstraint('quantity > 0', name='quantity_check')
