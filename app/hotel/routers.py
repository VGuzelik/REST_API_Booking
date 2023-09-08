from fastapi import APIRouter

from app.hotel.crud import HotelCRUD
from app.hotel.schemas import SHotel

router = APIRouter(prefix='/hotels', tags=['Hotels'])


@router.get('')
async def get_hotels() -> list[SHotel]:
    return await HotelCRUD().get_all_obj()


@router.get('/{hotel_id}')
async def get_booking_by_id(hotel_id: int) -> SHotel:
    return await HotelCRUD().get_obj_by_id(hotel_id)


