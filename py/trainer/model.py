import paddle
from paddle import nn
from paddle.nn import functional as F

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