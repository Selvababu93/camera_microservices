from pydantic import BaseModel

class CameraBase(BaseModel):
    brand : str
    model : str

    class Config:
        from_attributes = True


class CameraCreate(CameraBase):
    pass

class CameraRead(CameraBase):
    pass

class CameraModelUpdate(BaseModel):
    model : str