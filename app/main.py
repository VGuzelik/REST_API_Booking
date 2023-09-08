import uvicorn
from fastapi import FastAPI, Depends

from app.hotel.schemas import HotelSearchArgs

from app.booking.routers import router as router_bookings
from app.hotel.routers import router as router_hotels
from app.user.routers import router as router_user


app = FastAPI()

app.include_router(router_user)
app.include_router(router_bookings)
app.include_router(router_hotels)



# @app.get('/hotel')
# def get_hotels(search_args: HotelSearchArgs = Depends()):
#     return {'search_args': search_args}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )
