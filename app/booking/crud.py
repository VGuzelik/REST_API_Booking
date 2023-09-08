from sqlalchemy import select

from app.db import async_session_maker
from app.booking.models import Booking
from app.common.crud import BaseCRUD


class BookingCRUD(BaseCRUD):
    model = Booking
