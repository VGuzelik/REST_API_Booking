from app.common.crud import BaseCRUD
from app.image.models import ImagesHotel, ImagesRoom


class ImageHotelCRUD(BaseCRUD):
    _model = ImagesHotel


class ImageRoomCRUD(BaseCRUD):
    _model = ImagesRoom


