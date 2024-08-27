import paddle
import model as model_module

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
    return paddle.to_tensor(target_list, dtype=paddle.float32)


def load_model(path):
    state_dict = paddle.load(path)
    net = model_module.Model()
    net.set_state_dict(state_dict)
    net.eval()
    return net


def predict(net, target):
    output = net(target)
    return (output.argmax() == paddle.to_tensor(1,dtype=paddle.int64)).item()