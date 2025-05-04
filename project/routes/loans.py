from fastapi import APIRouter
from project.schemas import LoanResponse
from project.utils import read_loans, read_users


loansRouter =APIRouter(prefix="/api/loans", tags=["Loans"])

@loansRouter.get("/", response_model=list[LoanResponse])
async def get_loans():
    loans = read_loans()
    users = read_users()

    user_map = {}
    for user in users:
        user_map[user["id"]] = user

    response = []
    for loan in loans:
        user_data = user_map.get(loan["user_id"])
        loan["user"] = user_data  # attach user to loan
        response.append(LoanResponse(**loan))

    return response
