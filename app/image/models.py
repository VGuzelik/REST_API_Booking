from sqlalchemy import Column, Integer, String, ForeignKey

from app.db import Base


class ImagesHotel(Base):
    __tablename__ = 'images_hotel'

    id = Column(Integer, primary_key=True)
    image_url = Column(String, unique=True, nullable=False)
    hotel_id = Column(ForeignKey('hotel.id', ondelete='cascade'))


