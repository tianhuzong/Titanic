import paddle
from loguru import logger
def build_paddle_input(data):
    tensor = paddle.to_tensor(data)
    logger.debug(tensor)
    return tensor

def load_model(model_path):
    "load model"
    model = paddle.jit.load(model_path)
    return model

def predict(model, data):
    data = build_paddle_input(data)
    pred_probs = model(data)
    pred_numpy = pred_probs.numpy()
    return (pred_numpy.argmax(1) == 1).all()