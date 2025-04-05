from fastapi import APIRouter


router = APIRouter(
    prefix="/raspberry-awards",
    tags=["raspberry-awards"],
)

@router.get("/")
async def get_raspberry_awards():
    return {"message": "Prêmios"}