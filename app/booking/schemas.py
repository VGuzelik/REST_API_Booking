from dataclasses import dataclass, field
from datetime import date

from db import async_session_maker
from exceptions import RoomCannotBeBlocked
from hotel.room.models import Room
from pydantic import BaseModel
from sqlalchemy import and_, func, or_, select

from app.booking.models import Booking


class SBooking(BaseModel):

    id: int
    room_id: int
    user_id: int
    date_to: date
    date_from: date
    price: int
    total_days: int
    total_cost: int


@dataclass
class BookingArgs:
    room_id: int
    date_from: date
    date_to: date
    price: int = field(init=False)

    async def check_availability_rooms(self):

        async with async_session_maker() as session:
            booked_rooms = select(Booking).where(
                and_(
                    Booking.room_id == self.room_id,
                    or_(
                        and_(
                            Booking.date_from >= self.date_from,
                            Booking.date_from <= self.date_to,
                        ),
                        and_(
                            Booking.date_from <= self.date_from,
                            Booking.date_to > self.date_from,
                        )
                    )
                )
            ).cte('booked_rooms')

            get_rooms_left = select(
                Room.quantity - func.count(booked_rooms.c.room_id)
            ).select_from(Room).join(
                booked_rooms, isouter=True
            ).where(
                Room.id == self.room_id
            ).group_by(Room.quantity, booked_rooms.c.room_id)

            rooms_left = await session.execute(get_rooms_left)

            rooms_left: int = rooms_left.scalar()

            if rooms_left <= 0:
                raise RoomCannotBeBlocked

            get_price = select(Room.price).filter_by(id=self.room_id)
            price = await session.execute(get_price)
            self.price = price.scalar()
            return self
