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
    status: Literal["active", "inactive"]
    createdAt: str

class LoanCreate(BaseModel):
    amount: float
    userId: str

class LoanResponse(BaseModel):
    id: str
    amount: float
    status: str
    createdAt: str
    user: UserResponse | str

class UsersOverview(BaseModel):
    totalCount: int
    activeCount: int
    inactiveCount: int
    usersWithLoansCount: int