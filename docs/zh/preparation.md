# 预备

这是预备章节,在本章节,我们要完成环境的准备,依赖的安装.

## 要求环境
以下为建议的环境,具体下限多少我不知道
- python >= 3.8
- node >= 16.0.0
## 安装依赖

### 安装python依赖
安装python依赖建议使用虚拟环境,不知道怎么创建虚拟环境的话请STFW.
```bash
# 假定已经在项目的根目录下,并已经进入了虚拟环境
cd py
python -m pip install -r requirements.txt
# 这样之后就可以运行了
# python cli.py runapp -f onnx -m models/onnx_model/titan.onnx # 这个命令到时候再解释
```

### 安装node依赖
请根据需要选择你的node包管理器,这里我使用npm和yarn做演示
```bash
# 假定已经在项目的根目录下
# npm演示
cd vue/titan_web
npm install
# 这样之后就可以运行了
# npm run dev
```
```bash
# 假定已经在项目的根目录下
# yarn演示
cd vue/titan_web
yarn install
# 这样之后就可以运行了
# yarm dev
```

如果运行到这里没问题的话,那么恭喜你,已经成功地安装完依赖了.
请前往下一章[命令行工具使用教程](./cli.md)
