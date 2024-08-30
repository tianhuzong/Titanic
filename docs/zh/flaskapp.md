<h1 align="center">flask部署教程</h1>

本章节我们介绍flask的部署

老实说呢,我觉得这一章其实也没什么好说的,因为呢运行方法前面也有讲过了.

## 命令行运行
我们运行`python app.py --help`
```zsh
➜  py git:(main) ✗ python app.py --help
Usage: app.py [OPTIONS]

Options:
  -f, --framework [paddle|onnx]  The framework to use for prediction (paddle
                                 or onnx) 
  -m, --model_path TEXT          The path to the model file, If it is a model
                                 of flying slurry frame, please enter the file
                                 name, for example,
                                 models/paddle_model/model_titan (if your
                                 model is model_titan.pamodel).
  --host TEXT                    The host to run the app on
  --port INTEGER                 The port to run the app on
  --debug                        Whether to run the app in debug mode
  --help                         Show this message and exit.
```

可以发现还是指定这些参数.
不过！我这一次这些参数都没有设置必须填写,也就是说`python app.py`也可以正常运行
**默认值** :
- -f paddle
- -m models/paddle_model/model_titan
- --host 0.0.0.0
- --port 8000
所以运行`python app.py`等价于`python app.py -f paddle -m models/paddle_model/model_titan --host 0.0.0.0 --port 8000`

## 后台运行