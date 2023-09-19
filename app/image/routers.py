from fastapi import APIRouter, UploadFile

import shutil

from app.image.crud import ImagesHotel

router = APIRouter(prefix='/image', tags=['image'])


@router.post('/hotel', status_code=201)
async def add_image_hotel(hotel_id: int, file: UploadFile):
    image_url: str = f'static/images/{file.file.name}.webp'

    with open(image_url, 'wb+') as file_object:
        shutil.copyfileobj(file.file, file_object)

        await ImagesHotel.create_obj(
            image_url=image_url, hotel_id=hotel_id
        )


