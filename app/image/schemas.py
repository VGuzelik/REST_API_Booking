from pydantic import BaseModel


class SImage(BaseModel):
    image_url: str

