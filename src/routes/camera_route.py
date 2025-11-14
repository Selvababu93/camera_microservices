from fastapi import APIRouter, HTTPException, status
from typing import Annotated, List
import schemas
from database import get_db, db_dependency
from models import CameraModel

router = APIRouter()


@router.get("/all", response_model=List[schemas.CameraRead])
def read_cameras(db: db_dependency):
    return db.query(CameraModel).all()


@router.post("/")
def create_camera(camera_create: schemas.CameraCreate, db: db_dependency):
    camera_create = CameraModel(model=camera_create.model, brand=camera_create.brand)
    db.add(camera_create)
    db.commit()
    db.refresh(camera_create)
    return camera_create

@router.patch("/update_model/{camera_id}", response_model=schemas.CameraRead)
def update_camera(camera_id : int, db: db_dependency, request: schemas.CameraModelUpdate):
    camera = db.query(CameraModel).filter(CameraModel.id == camera_id).first()
    if not camera:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Camera id not found")
    camera.model = request.model

    db.commit()
    return camera


@router.delete("/del/{camera_id}")
def delete_camera(camera_id: int, db: db_dependency):
    camera = db.query(CameraModel).filter(CameraModel.id == camera_id)

    if not camera:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Camera not found")
    camera.delete(synchronize_session=False)
    db.commit()

    return "Delete operation success"
