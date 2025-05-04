from fastapi import FastAPI
from .routes import users,loans,overview
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS from your frontend origin
# origins = [
#     "http://localhost:3000",  # React dev server
#     "https://your-frontend-domain.com"  # Replace with your deployed frontend URL
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users.router)
app.include_router(loans.loansRouter)
app.include_router(overview.router)