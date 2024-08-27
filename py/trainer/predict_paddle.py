import paddle

def build_paddle_input(data):
    data = paddle.to_tensor(data)
    data = paddle.unsqueeze(data, axis=0)
    return data

def load_model(model_path):
    "load model"
    model = paddle.jit.load(model_path)
    return model

def predict(model, data):
    data = build_paddle_input(data)
    pred_probs = model(data)
    pred_label = paddle.argmax(pred_probs, axis=1)
    pred_numpy = pred_label.numpy()
    return (pred_numpy.argmax(1) == 1).all()