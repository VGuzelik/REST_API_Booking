from sqlalchemy import select, func
from sqlalchemy.dialects.postgresql import array_agg

from app.common.crud import BaseCRUD
from db import async_session_maker
from app.hotel.room.models import Room
from app.image.models import ImagesRoom


class RoomCRUD(BaseCRUD):
    _model = Room

    @classmethod
    async def get_all_rooms_by_hotel_id(cls, hotel_id: int):
        async with async_session_maker() as session:
            query = select(
                cls._model.__table__.columns,
                array_agg(
                    func.distinct(ImagesRoom.image_url)
                ).label('image_urls'),
            ).select_from(cls._model).outerjoin(ImagesRoom).where(
                cls._model.hotel_id == hotel_id
            ).group_by(cls._model.id)

            rooms = await session.execute(query)
            return rooms.mappings().all()
