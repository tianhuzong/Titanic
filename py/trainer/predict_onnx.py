import onnxruntime as ort
import numpy as np

def build_onnx_input(input_data):
    input_data = np.array(input_data)
    input_data = input_data.astype(np.float32)
    input_data = input_data.reshape(1, -1)
    return input_data

def load_model(model_path):
    "create session"
    sess = ort.InferenceSession(model_path)
    return sess

def predict(sess, input_data):
    input_data = build_onnx_input(input_data)
    input_name = sess.get_inputs()[0].name
    output_name = sess.get_outputs()[0].name
    pred_onx = sess.run([output_name], {input_name: input_data.astype(np.float32)})[0]
    
    return (pred_onx.argmax(axis=1) == 1).all()