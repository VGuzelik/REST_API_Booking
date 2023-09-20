from fastapi import APIRouter

from app.hotel.room.crud import RoomCRUD

router = APIRouter()


@router.get('/{hotel_id}/rooms')
async def get_rooms(hotel_id: int):
    return await RoomCRUD.get_all_rooms_by_hotel_id(hotel_id)
