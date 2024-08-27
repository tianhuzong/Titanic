import numpy  as np
import pandas as pd
import paddle
import datas
import datasets
import model
import train as train_model

def start_train():
    pass
    train_data = pd.read_csv('./data/titan/train.csv')
    val_data = pd.read_csv('./data/titan/test.csv')
    full_data = datas.clean_data(train_data, val_data)
    train, test, val = datasets.get_datasets(full_data)
    train_loader, test_loader, val_loader = datasets.get_dataloader(train, test, val)
    
    net = model.Model()
    lossfn = paddle.nn.functional.cross_entropy
    
    train_model.train(net, max_epoch= 10000,  lossfn=lossfn,train_loader=train_loader,test_loader=test_loader)


if __name__ == '__main__':
    start_train()