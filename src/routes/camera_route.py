from fastapi import APIRouter
from typing import Annotated, List
import schemas
from database import get_db, db_dependency
from models import CameraModel

router = APIRouter()


@router.get("/all", response_model=List[schemas.CameraRead])
def read_cameras(session: db_dependency):
    return session.query(CameraModel).all()


@router.post("/")
def create_camera(camera_create: schemas.CameraCreate, db: db_dependency):
    camera_create = CameraModel(model=camera_create.model, brand=camera_create.brand)
    db.add(camera_create)
    db.commit()
    db.refresh(camera_create)
    return camera_create


