from app.common.crud import BaseCRUD
from app.image.models import ImagesHotel


class ImageCRUD(BaseCRUD):
    _model = ImagesHotel

