from fastapi import FastAPI, APIRouter

from app.api.routers import main_route

router = APIRouter()

app = FastAPI()

app.include_router(main_route)
