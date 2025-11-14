import os
from fastapi import FastAPI
import uvicorn
from models import CameraModel
from database import engine, Base
from routes import camera_route, sensors_route

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(camera_route.router, prefix='/Camera', tags=['Camera'])
app.include_router(sensors_route.router, prefix='/Sensors', tags=['Sensors'])



@app.get("/")
def root():
    return {
        "msg" : "hello Wealth!!!",
        "App Name" : os.getenv("APP_NAME"),
        "environment" : os.getenv("ENVIRONMENT")}



if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)