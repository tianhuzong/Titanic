import os
import json
from flask import Flask, request
from flask_cors import CORS
from trainer import predict as predict_module
from loguru import logger
import time
import click
app = Flask(__name__)
CORS(app) 
global model
global frame

@app.get("/")
def read_root():
    return """<h1>Hello, Welcome to Titanic Survival Prediction API, Please use POST method to predict the survival probability of a passenger.</h1>"""

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
    res = (predict_module.predict(frame, model, input_data))
    timei = time.time()
    #转成日期格式xxxx-xx-xx HH:MM:SS
    timei = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timei))
    logger.info(f"{timei}  {res}")
    return {"result":res}
    
def run_app(framework, model_path, host="0.0.0.0", port=8000, debug=True):
    global model, frame
    model = predict_module.load_model(framework, model_path)
    frame = framework

    app.run(host=host, port=port, debug=debug)



@click.command()
@click.option('-f','--framework' ,type=click.Choice(['paddle', 'onnx']) ,help='The framework to use for prediction (paddle or onnx)', default="onnx")
@click.option('-m','--model_path',help='The path to the model file, If it is a model of flying slurry frame, please enter the file name, for example, models/paddle_model/model_titan (if your model is model_titan.pamodel).', default="models/onnx_model/titan.onnx")
@click.option('--host', default="0.0.0.0", help='The host to run the app on')
@click.option('--port', default=8000, help='The port to run the app on')
@click.option('--debug', default=False, help='Whether to run the app in debug mode', is_flag=True)
def runapp(framework, model_path, host, port, debug):
    run_app(framework, model_path, host, port, debug)

if __name__ == "__main__":
    runapp()