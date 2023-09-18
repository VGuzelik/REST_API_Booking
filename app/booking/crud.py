from app.booking.models import Booking
from app.common.crud import BaseCRUD


class BookingCRUD(BaseCRUD):
    _model = Booking
