from fastapi import APIRouter
from fastapi.responses import JSONResponse
from project.schemas import UsersOverview
from project.utils import read_users

router = APIRouter(prefix="/api/overviews", tags=["Users"])

@router.get("/users", response_model=UsersOverview)
def get_users_overview():
    try:
        users = read_users()
        if len(users) == 0:
            return  UsersOverview(
            totalCount=0,
            activeCount=0,
            inactiveCount=0,
            usersWithLoansCount=0
        )
        active_count = 0
        inactive_count = 0
        users_with_loans_count = 0

        for user in users:
            if user["status"] == "active":
                active_count += 1
            elif user["status"] == "inactive":
                inactive_count += 1

            if "loans" in user and len(user["loans"]) > 0:
                users_with_loans_count += 1

        return UsersOverview(
            totalCount=len(users),
            activeCount=active_count,
            inactiveCount=inactive_count,
            usersWithLoansCount=users_with_loans_count
        )

    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=500,
            content={"detail": f"Internal server error: {str(e)}"},
        )
