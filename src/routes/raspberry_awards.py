from fastapi import APIRouter
from src.services import raspberry_awards

router = APIRouter(
    prefix="/raspberry-awards",
    tags=["raspberry-awards"],
)

@router.get("/")
async def get_raspberry_awards():
    return raspberry_awards.get_raspberry_min_max_awards()