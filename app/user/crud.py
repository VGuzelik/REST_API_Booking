from app.common.crud import BaseCRUD
from app.user.models import User


class UserCRUD(BaseCRUD):
    _model = User
