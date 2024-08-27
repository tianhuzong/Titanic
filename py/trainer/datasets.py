from paddle.io import Dataset, random_split, DataLoader
import paddle
import pandas as pd
import numpy as np

class TrainData(Dataset):
    def __init__(self, train_data):
        super().__init__()
        self.data = []
        alive_tensor = paddle.to_tensor(1,dtype=paddle.int64)
        dead_tensor = paddle.to_tensor(0,dtype=paddle.int64)
        # 张量按照以下顺序
        # 性别 年龄 票价 三个港口(C Q S) 三个票的类别(1 2 3) 六个人的等级(Master Miss Mr Mrs Officer Royalty) 客舱号(A-T and U) 家庭大小 单身 小号  大号 
        for x in train_data.values.tolist():
            alive = x.pop(0)
            self.data.append([paddle.to_tensor(x,dtype=paddle.float64), alive_tensor if alive == 1 else dead_tensor])
        
    def __getitem__(self, index):
        return self.data[index]
    
    def __len__(self):
        """
        步骤四：实现 __len__ 函数，返回数据集的样本总数
        """
        return len(self.data)
    

class ValData(Dataset):
    def __init__(self, val_data):
        super().__init__()
        self.data = []
        # 张量按照以下顺序
        # 性别 年龄 票价 三个港口(C Q S) 三个票的类别(1 2 3) 五个人的等级(Master Miss Mr Mrs Officer Royalty) 客舱号(A-T and U) 家庭大小 单身 小号  大号 
        for x in val_data.values.tolist():
            x.pop(0)
            self.data.append(paddle.to_tensor(x,dtype=paddle.float64))
        
    def __getitem__(self, index):
        return self.data[index]
    
    def __len__(self):
        """
        步骤四：实现 __len__ 函数，返回数据集的样本总数
        """
        return len(self.data)
    

import paddle

def getdatasets(full):
    """用于获得train 和 val数据集"""
    train = full.dropna(subset=['Survived'])
    # 使用布尔索引过滤出 'Survived' 列为空值的行
    val = full[full['Survived'].isna()]
    
    train_dataset = TrainData(train)
    val_dataset = ValData(val)
    
    return train_dataset, val_dataset

def get_datasets(full):
    train_dataset, val_dataset = getdatasets(full)
    
    # 使用 train_dataset 的长度计算划分比例
    train_len = int(len(train_dataset) * 0.8)
    test_len = len(train_dataset) - train_len
    
    train_dataset, test_dataset = paddle.io.random_split(train_dataset, [train_len, test_len])
    
    return train_dataset, test_dataset, val_dataset



def get_dataloader(train, test, val, batch_size=64):
    """用于获得train 和 val数据加载器"""
    # 训练数据加载器
    train_loader = paddle.io.DataLoader(train, batch_size=batch_size,return_list=True,shuffle=True)
    test_loader = paddle.io.DataLoader(test, batch_size=1,return_list=True,shuffle=True)
    val_loader = paddle.io.DataLoader(val, batch_size=batch_size,return_list=True,shuffle=True)
    return train_loader, test_loader, val_loader

