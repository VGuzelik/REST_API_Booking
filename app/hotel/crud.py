from app.common.crud import BaseCRUD
from app.hotel.models import Hotel


class HotelCRUD(BaseCRUD):
    model = Hotel
