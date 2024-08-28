import os
import json
from flask import Flask, request
from flask_cors import CORS
from trainer import predict as predict_module

app = Flask(__name__)
CORS(app) 
global model
global frame

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
def read_predict():

    data_dict = {
        "sex" : (request.json.get("sex")),
        "age" : (request.json.get("age")),
        "fare" : (request.json.get("fare")),
        "embarked" : (request.json.get("embarked")),
        "ticket_class" : (request.json.get("ticket_class")),
        "name" : request.json.get("name"),
        "cabin" : request.json.get("cabin"),
        "family_size" : request.json.get("family_size"),
    }
    none_keys = [key for key, value in data_dict.items() if value is None]

    if none_keys:
        return json.dumps({"error": "Missing input data, The missing fields are {}".format(none_keys)},ensure_ascii=False)

    sex = int(data_dict.get("sex"))
    age = int(data_dict.get("age"))
    fare = float(data_dict.get("fare"))
    embarked = int(data_dict.get("embarked"))
    ticket_class = int(data_dict.get("ticket_class"))
    name = request.json.get("name")
    cabin = request.json.get("cabin")
    family_size = int(data_dict.get("family_size"))

    input_data = predict_module.build_tensor(sex, age, fare, embarked, ticket_class, name, cabin, family_size)
    return {"result":(predict_module.predict(frame, model, input_data))}
    
def run_app(framework, model_path, host="0.0.0.0", port=8000, debug=True):
    global model, frame
    model = predict_module.load_model(framework, model_path)
    frame = framework

    app.run(host=host, port=port, debug=debug)

if __name__ == "__main__":
    run_app("paddle", "models/paddle_model/model_titan", "0.0.0.0", 8000, True)