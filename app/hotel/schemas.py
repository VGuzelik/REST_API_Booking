from dataclasses import dataclass
from datetime import date
from typing import Optional, List

# from fastapi import Query
from pydantic import BaseModel, Field


# @dataclass
# class HotelSearchArgs:
#     location: str
#     # data_from: date
#     # date_to: date
#     # # has_spa: Optional[bool] = None
#     # # stars: Optional[int] = Query(None, ge=1, le=5)

class SHotelCreate(BaseModel):

    name: str
    location: str
    services: Optional[list] = Field(default=None)
    room_quantity: int


class SHotelRepresention(BaseModel):

    id: int
    name: str
    location: str
    services: Optional[list] = Field(default=None)
    room_quantity: int
    image_urls: Optional[list[str | None]] = Field(default=None)
