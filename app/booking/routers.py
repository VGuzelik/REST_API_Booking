from datetime import date

from fastapi import APIRouter, Depends

from app.booking.crud import BookingCRUD
from app.booking.schemas import SBooking, BookingArgs

from app.user.models import User
from app.user.dependencies import get_current_user

router = APIRouter(prefix='/bookings', tags=['Bookings'])


@router.get('')
async def get_bookings(
        user: User = Depends(get_current_user)
) -> list[SBooking]:

    return await BookingCRUD.get_all_obj(user_id=user.id)


@router.post('')
async def add_bookings(
        user: User = Depends(get_current_user),
        booking_args: BookingArgs = Depends(),
) -> SBooking:

    verified_data = await booking_args.check_availability_rooms()

    return await BookingCRUD.create_obj(
        user_id=user.id,
        room_id=verified_data.room_id,
        date_to=verified_data.date_to,
        date_from=verified_data.date_from,
        price=verified_data.price,
    )







