from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from uuid import uuid4
from datetime import datetime
from ..models import User
from ..schemas import UserCreate, UserResponse
from ..utils import read_users, write_users, hash_password
from project.schemas import UserCreate, UserResponse
from project.utils import read_users

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.post("/api/users", response_model=UserResponse)
def create_user(user: UserCreate):
    try:
        users = read_users()
        for u in users:
            if u['username'].lower() == user.username.lower():
                raise HTTPException(status_code=400, detail="User already exists")

        new_user = User(
            id=str(uuid4()),
            username=user.username,
            email=user.email,
            organization=user.organization,
            phoneNumber=user.phoneNumber,
            status=user.status,
            createdAt=datetime.utcnow().isoformat(),
            password=hash_password(user.password)
        )

        users.append(new_user.to_dict())
        write_users(users)

        return UserResponse(**new_user.to_dict())

    except HTTPException as http_err:
        raise http_err  # Re-raise known errors

    except Exception as e:
        # For unexpected internal errors
        return JSONResponse(
            status_code=500,
            content={"detail": f"Internal server error: {str(e)}"},
        )

@router.get("/api/users", response_model=list[UserResponse])
def list_users():
    users = read_users()
    return [UserResponse(**{k: v for k, v in u.items() if k != "password"}) for u in users]

@router.get("/api/users/{user_id}", response_model=UserResponse)
def get_user(user_id: str):
    users = read_users()
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(**{k: v for k, v in user.items() if k != "password"})

@router.patch("/api/users/{user_id}/toggle-status", response_model=UserResponse)
def toggle_status(user_id: str):
    users = read_users()
    for user in users:
        if user["id"] == user_id:
            user["status"] = "inactive" if user["status"] == "active" else "active"
            write_users(users)
            return UserResponse(**{k: v for k, v in user.items() if k != "password"})
    raise HTTPException(status_code=404, detail="User not found")
