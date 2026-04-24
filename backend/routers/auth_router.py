from fastapi import APIRouter

auth = APIRouter()

@auth.post("/login")
async def login(
) -> any:
    pass

@auth.post("/register")
async def register(
) -> any:
    pass