import importlib


def build_tensor(
    sex : int, # 男1 女0
    age : int, # 年龄
    fare : float, # 票价
    embarked : int, # 登船港口 C=1 Q=2 S=3
    ticket_class : int, # 船票类别 1 2 3
    name : str, # 身份 Master Miss Mr Mrs Officer Royalty
    cabin : str, # 船舱号 A-T and U
    family_size : int, # 家庭人数 包含自己
):
    pass
    target_list = []
    target_list.append(sex)
    target_list.append(age)
    target_list.append(fare)
    
    temp = [0,0,0]
    temp[embarked - 1] = 1
    target_list.extend(temp)
    
    temp = [0,0,0]
    temp[ticket_class - 1] = 1
    target_list.extend(temp)
    
    temp = "Master Miss Mr Mrs Officer Royalty".split(" ")
    t2 = [0,0,0,0,0,0]
    t2[temp.index(name)] = 1
    target_list.extend(t2)
    
    temp = "A B C D E F G T U".split(" ")
    t2 = [0,0,0,0,0,0,0,0,0]
    t2[temp.index(cabin)] = 1
    target_list.extend(t2)
    
    target_list.append(family_size)
    
    temp = [0,0,0]
    temp[0] = 1 if family_size == 1 else 0
    temp[1] = 1 if 2<= family_size <= 4 else 0
    temp[2] = 1 if family_size > 4 else 0
    target_list.extend(temp)
    return [target_list]

def load_model(framework, model_path):
    """
    加载模型
    :param framework: 推理框架 onnx or paddle
    :param model_path: 模型路径 如果是onnx 则为onnx模型文件路径 如果是paddle 则为paddle模型名(不包含后缀,且确保模型参数和模型结构在同一目录下)
    :return : 返回模型对象
    """
    if framework == "onnx":
        from . import predict_onnx as pre 
    elif framework == "paddle":
        from . import predict_paddle as pre
    return pre.load_model(model_path)   

def predict(framework, model, target):
    """
    预测函数
    :param framework: 推理框架 onnx or paddle
    :param model: 模型
    :param target: 输入数据 格式为列表 长度为28
    :return: 预测结果 True 代表 生还 False 代表  死亡
    """
    if framework == "onnx":
        from . import predict_onnx as pre 
    elif framework == "paddle":
        from .import predict_paddle as pre
    output = pre.predict(model,target)
    return bool(output)