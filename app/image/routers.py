from fastapi import APIRouter, UploadFile

import shutil
import uuid

from app.image.crud import ImageHotelCRUD, ImageRoomCRUD

router = APIRouter(prefix='/image', tags=['image'])


@router.post('/hotel', status_code=201)
async def add_image_hotel(hotel_id: int, file: UploadFile):
    image_url: str = f'static/images/{uuid.uuid4()}.webp'

    with open(image_url, 'wb+') as file_object:
        shutil.copyfileobj(file.file, file_object)

        await ImageHotelCRUD.create_obj(
            image_url=image_url, hotel_id=hotel_id
        )


@router.post('/room', status_code=201)
async def add_image_hotel(room_id: int, file: UploadFile):
    image_url: str = f'static/images/{uuid.uuid4()}.webp'

    with open(image_url, 'wb+') as file_object:
        shutil.copyfileobj(file.file, file_object)

        await ImageRoomCRUD.create_obj(
            image_url=image_url, room_id=room_id
        )


