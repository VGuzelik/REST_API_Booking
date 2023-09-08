from fastapi import APIRouter, Depends

from app.booking.crud import BookingCRUD
from app.booking.schemas import SBooking

from app.user.models import User
from app.user.dependencies import get_current_user

router = APIRouter(prefix='/bookings', tags=['Bookings'])


@router.get('')
async def get_bookings(user: User = Depends(get_current_user)):
    print(user)


@router.get('/{booking_id}')
async def get_booking_by_id(booking_id: int) -> SBooking | None:
    return await BookingCRUD().get_obj_by_id(booking_id)

