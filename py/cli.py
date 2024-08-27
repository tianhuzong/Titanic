import click
import typing
import os
import subprocess
from trainer import predict as predict_module

@click.group()
def cli():
    """The Titantic CLI"""
    pass

input_arg_types = (int, float, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, int, 
)

@cli.command()
@click.option('-f','--framework', prompt='Please enter the framework',type=click.Choice(['paddle', 'onnx']) ,help='The framework to use for prediction (paddle or onnx)',required=True)
@click.option('-m','--model_path', prompt='Please enter the model path',help='The path to the model file',required=True)
@click.argument('input_args',  type=input_arg_types, nargs=28)
def predict(framework, model_path, input_args):
    """Predict the survival of a passenger based on their input data"""
    model = predict_module.load_model(model_path)
    res = predict_module.predict(framework, model, input_args)
    click.echo("The passenger {} survive.".format("can" if res else "cannot"))

@cli.command()
def runapp(framework, model_path):
    os.environ["titanic_fastapi_app_framework"] = framework
    os.environ["titanic_fastapi_app_model_path"] = model_path
    subprocess.run(["uvicorn","app:app","--reload"])
    pass

if __name__ == '__main__':
    cli()