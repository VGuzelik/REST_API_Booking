from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    password: str


class SUserRepresentation(BaseModel):
    id: int
    email: EmailStr
