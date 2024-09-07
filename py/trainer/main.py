import numpy  as np
import pandas as pd
import paddle
import datas
import datasets
import model
import train as train_model

def start_train():
    # 加载数据集
    train_data = pd.read_csv('./data/titan/train.csv')
    val_data = pd.read_csv('./data/titan/test.csv')
    # 数据清洗
    full_data = datas.clean_data(train_data, val_data)
    # 创建数据集
    train, test, val = datasets.get_datasets(full_data)
    # 创建加载器
    train_loader, test_loader, val_loader = datasets.get_dataloader(train, test, val)
    # 初始化模型和损失函数
    net = model.Model()
    lossfn = paddle.nn.functional.cross_entropy
    # 开始训练
    train_model.train(net, max_epoch= 10000,  lossfn=lossfn,train_loader=train_loader,test_loader=test_loader)


if __name__ == '__main__':
    start_train()