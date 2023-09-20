from sqlalchemy import select, func
from sqlalchemy.orm import joinedload
from sqlalchemy.dialects.postgresql import array_agg

from app.common.crud import BaseCRUD
from app.hotel.models import Hotel
from db import async_session_maker
from app.image.models import ImagesHotel


class HotelCRUD(BaseCRUD):
    _model = Hotel

    @classmethod
    async def get_hotels_by_location(cls, location: str):
        async with async_session_maker() as session:
            query = select(
                cls._model.__table__.columns,
                array_agg(
                    func.distinct(ImagesHotel.image_url)
                ).label('image_urls'),
            ).select_from(cls._model).outerjoin(ImagesHotel).where(
                cls._model.location.like(f'%{location}%')
            ).group_by(cls._model.id)

            hotels = await session.execute(query)

            return hotels.mappings().all()

    @classmethod
    async def get_obj_by_id(cls, hotel_id: int):
        async with async_session_maker() as session:
            hotel = await session.execute(
                select(
                    cls._model.__table__.columns,
                    array_agg(
                        func.distinct(ImagesHotel.image_url)
                    ).label('image_urls'),
                ).select_from(cls._model).outerjoin(ImagesHotel).where(
                    cls._model.id == hotel_id
                ).group_by(cls._model.id)
            )
            return hotel.fetchone()
