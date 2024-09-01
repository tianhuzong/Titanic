<h1 align="center">训练教程</h1>

本章节是对训练代码的一些讲解,本章节不看也罢.

首先我们来看目录结构(`项目根目录/py`)
```
trainer
    |--- __init__.py 这个文件啥都没有,详细作用不用我解释了吧
    |--- datas.py 用于对训练数据进行清洗
    |--- datasets.py 数据集的定义,还有获取数据集和数据加载器的函数.
    |--- model.py 定义了网络架构.
    |--- predict_paddle.py paddle框架的推理接口.
    |--- predict_onnx.py onnx框架的推理接口.
    |--- predict.py 用于实现一个可以调用两个框架预测的接口.
    |--- train.py 定义一个训练函数和测试函数.
    |--- main.py 用来启动训练的代码.
```

## datas.py

首先看`datas.py`,这个文件的大部分内容可以在网上找到，但是不同的网站的实现方法可能不一样.
我的代码是参照这一个的代码的:[泰坦尼克号生存预测分析](https://zhuanlan.zhihu.com/p/371416196)

## datasets.py

然后来看`dataset.py`.
这个文件文件中我定义了两个类`TrainDara`和`ValData`.
因为我不知道这个`ValData`的作用,所以到最后可能用不上,因为删除这个代码需要修改很多东西,所以我保留了下来,等人来发现他的用处.
这里定义了三个函数:
| 函数 | 说明 |
| --- | --- |
| `getdatasets(full)` | 传入一个pandas.DataFrame, 将其分割为train_data和val_data|
| `get_datasets(full)` | 传入一个pandas.DataFrame, 将其分割为train_data,test_data和val_data,我们一般使用这个|
| `get_dataloader(train, test, val, batch_size=64)` | 用于生成三个数据集的DataLoader,并制定batch_size |

我们一般使用`get_datasets`来获取,传入的参数时在datas.py中定义的`clean_data`函数的返回值.

## model.py

`model.py`定义了我们的网络结构:
```python
class Model(nn.Layer):
    def __init__(self):
        super(Model, self).__init__()
        self.fc1 = nn.Linear(28, 120)
        self.fc2 = nn.Linear(120, 300)
        self.fc3 = nn.Linear(300, 84)
        self.fc4 = nn.Linear(84, 2)
        self.dropout = nn.Dropout(0.3)

    def forward(self, x):
        x = x.astype(paddle.float32)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return F.softmax(x)
```
这个网络结构在网上搜索二分类模型基本可以找到,这个模型会输出一个shape为`[1, 2]`的向量
使用`output.argmax(1).item()`可以获得结果,生为1,死为0.

## predict_paddle.py predict_onnx.py predict.py
`predict_paddle.py`和`predict_onnx.py`都暴露了一个`load_model`和`predict`接口给`predict.py`调用,我们只要直接通过`predict.py`调用即可
以下是`predict.py`的说明:
| 函数 | 说明 |
| --- | --- |
| `load_model(framework, model_path)` | framework: 推理框架 onnx or paddle;<br />model_path: 模型路径<br />如果是onnx 则为onnx模型文件路径 如果是paddle 则为paddle模型名(不包含后缀,且确保模型参数和模型结构在同一目录下) |
| `predict(framework, model, target)` | framework: 推理框架 onnx or paddle;<br />model: 模型;<br />target: 输入数据 格式为列表 长度为28;预测结果 True 代表 生还 False 代表  死亡 |

这个`model_path`也许还让人有点晕,意思是说
- 如果你的`framework`传入的框架是`onnx`那就传入那个文件,例如`models/onnx_model/titan.onnx`
- 如果你的`framework`传入的框架是`paddle`那就传入那些模型的文件名不包含前缀,例如`models/paddle_model/model_titan`

## train.py
定义两个函数:
| 函数 | 说明 |
| --- | --- |
| `train(model, max_epoch, lossfn, train_loader, test_loader)` | 训练函数,依次传入模型对象, 训练轮次, 损失函数, 训练数据集加载器, 测试数据集加载器,往后会考虑加入终端训练后恢复训练的代码 |
| `test(model, lossfn, test_loader, dataname="测试")` | 测试函数,传入模型,损失函数,测试集加载器,测试数据集名称(在输出结果时会用到) |

由于本人是新手玩深度学习,所以对于超参数的调整都整不明白,我自己训练的模型在测试集上的准确率一般只有80%~90%,一直提不上去,想要训练更高准确率可以根据自己的需要调整训练代码训练.

## model.py
这个文件是整个训练器的核心,通过启动这个程序可以自动开始训练,你可以根据需要对这里面代码进行调整后训练.