import numpy  as np
import pandas as pd
import paddle
import datas
import datasets
import model
import train as train_model

def main():
    pass
    train_data = pd.read_csv('./data/titan/train.csv')
    val_data = pd.read_csv('./data/titan/test.csv')
    full_data = datas.clean_data(train_data, val_data)
    train, test, val = datasets.get_datasets(full_data)
    train_loader, test_loader, val_loader = datasets.get_dataloader(train, test, val)
    
    net = model.Model()
    net.set_state_dict(paddle.load("checkpoints/model_10.pdparams"))
    opt = paddle.optimizer.SGD(learning_rate=0.005, parameters=net.parameters())
    lossfn = paddle.nn.functional.cross_entropy
    
    train_model.train(net, max_epoch= 10000,  lossfn=lossfn,opt=opt,train_loader=train_loader,test_loader=test_loader)


if __name__ == '__main__':
    main()