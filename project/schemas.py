from pydantic import BaseModel, EmailStr, constr
from typing import Literal


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    organization: str
    phoneNumber: str
    status: Literal["active", "inactive"]
    password: str

class UserResponse(BaseModel):
    id: str
    username: str
    email: EmailStr
    organization: str
    phoneNumber: str
    status: Literal['active', 'inactive']
    createdAt: str
