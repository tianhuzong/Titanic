import paddle

def build_paddle_input(data):
    data = paddle.to_tensor(data)
    data = paddle.unsqueeze(data, axis=0)
    return data

def predict(model_path, data):
    data = build_paddle_input(data)
    model = paddle.jit.load(model_path)
    pred_probs = model(data)
    pred_label = paddle.argmax(pred_probs, axis=1)
    pred_numpy = pred_label.numpy()
    return (pred_numpy.argmax(1) == 1).all()