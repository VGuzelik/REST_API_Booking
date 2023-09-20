from fastapi import APIRouter

from app.hotel.crud import HotelCRUD
from app.hotel.schemas import SHotelRepresention
from app.hotel.room.routers import router as router_rooms

router = APIRouter(prefix='/hotels', tags=['Hotels'])

router.include_router(router_rooms)


@router.get('')
async def get_hotels(location: str) -> list[SHotelRepresention]:
    return await HotelCRUD.get_hotels_by_location(location=location)


@router.get('/{hotel_id}')
async def get_hotel_by_id(hotel_id: int) -> SHotelRepresention:
    hotel = await HotelCRUD().get_obj_by_id(hotel_id=hotel_id)
    return hotel
