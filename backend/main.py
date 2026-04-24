from fastapi import FastAPI
from routers import auth, traveling

app = FastAPI()

app.include_router(auth)
app.include_router(traveling)

engine = None
