import os
from fastapi import FastAPI
from pydantic import BaseModel
from trainer import predict as predict_module

app = FastAPI()
framework = os.getenv("titanic_fastapi_app_framework")
model_path = os.getenv("titanic_fastapi_app_model_path")

class Model_Input(BaseModel):
    sex: int
    age: int
    fare: float 
    embarked: str 
    pclass: str
    title: str
    cabin: str 
    family_size: int 

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
def read_predict(item: Model_Input):
    return item
