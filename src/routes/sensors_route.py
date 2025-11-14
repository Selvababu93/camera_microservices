from fastapi import APIRouter, Depends



router = APIRouter()



@router.get("/")
def sensor_root():
    return "Sensor root route"


