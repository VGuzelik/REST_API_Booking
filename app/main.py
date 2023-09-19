import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.booking.routers import router as router_bookings
from app.hotel.routers import router as router_hotels
from app.user.routers import router as router_user
from app.image.routers import router as router_image

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), 'static')

app.include_router(router_user)
app.include_router(router_bookings)
app.include_router(router_hotels)
app.include_router(router_image)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        reload=True
    )
