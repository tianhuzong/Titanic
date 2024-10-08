import click
import typing
import os
import subprocess
import app
from trainer import predict as predict_module

@click.group()
def cli():
    """The Titantic CLI"""
    pass

input_arg_types = (int, int, float, int, int, str, str, int)

@cli.command()
@click.option('-f','--framework', default='onnx', prompt='Please enter the framework',type=click.Choice(['paddle', 'onnx']) ,help='The framework to use for prediction (paddle or onnx)',required=True)
@click.option('-m','--model_path', default='models/onnx_model/titan.onnx', prompt='Please enter the model path',help='The path to the model file',required=True)
@click.argument('input_args',  type=input_arg_types, nargs=8)
def predict(framework, model_path, input_args):
    """
    Predict the survival of a passenger based on their input data\n
    The input args are:\n
        sex : int, # 男1 女0\n
        age : int, # 年龄\n
        fare : float, # 票价\n
        embarked : int, # 登船港口 C=1 Q=2 S=3\n
        ticket_class : int, # 船票类别 1 2 3\n
        name : str, # 身份 Master Miss Mr Mrs Officer Royalty\n
        cabin : str, # 船舱号 A-T and U\n
        family_size : int, # 家庭人数 包含自己\n
    """
    input_tensor = predict_module.build_tensor(*input_args)
    model = predict_module.load_model(framework, model_path)
    res = predict_module.predict(framework, model, input_tensor)
    click.echo("The passenger {} survive.".format("can" if res else "cannot"))

@cli.command()
@click.option('-f','--framework', prompt='Please enter the framework',type=click.Choice(['paddle', 'onnx']) ,help='The framework to use for prediction (paddle or onnx)',required=True)
@click.option('-m','--model_path', prompt='Please enter the model path',help='The path to the model file, If it is a model of flying slurry frame, please enter the file name, for example, models/paddle_model/model_titan (if your model is model_titan.pamodel).',required=True)
@click.option('--host', default="0.0.0.0", help='The host to run the app on',required=True)
@click.option('--port', default=8000, help='The port to run the app on',required=True)
@click.option('--debug', default=False, help='Whether to run the app in debug mode',required=True, is_flag=True)
def runapp(framework, model_path, host, port, debug):
    """Run the flask app"""
    app.run_app(framework, model_path, host=host, port=port, debug=debug)
    

if __name__ == '__main__':
    cli()