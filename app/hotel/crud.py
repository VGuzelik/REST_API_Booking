from sqlalchemy import select

from app.common.crud import BaseCRUD
from app.hotel.models import Hotel
from db import async_session_maker


class HotelCRUD(BaseCRUD):
    _model = Hotel

    @classmethod
    async def get_hotels_by_location(cls, location):
        async with async_session_maker() as session:
            query = select(cls._model).where(
                cls._model.location.like(f'%{location}%')
            )
            result = await session.execute(query)
            return result.scalars().all()
