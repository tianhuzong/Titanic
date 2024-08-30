# 命令行工具使用教程

在本章节我们会介绍py/cli.py这个命令行工具的使用方法

## 获取帮助讯息
运行`python cli.py --help`可以获得帮助信息
```zsh
➜  py git:(main) python ./cli.py 
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

  The Titantic CLI

Options:
  --help  Show this message and exit.

Commands:
  predict  Predict the survival of a passenger based on their input data
  runapp   Run the flask app
```
我们可以看到他为我们输出了信息,这个工具包含两个命令:`predict`和`runapp`,接下来我们来详细地说这两个命令.

## predict命令
这个命令用于推理,我们还是先看帮助信息
### 获取`predict`命令的帮助信息
运行`python cli.py predict --help`
```zsh
➜  py git:(main) ✗ python ./cli.py predict --help
Usage: cli.py predict [OPTIONS] INPUT_ARGS...

  Predict the survival of a passenger based on their input data

  The input args are:

      sex : int, # 男1 女0

      age : int, # 年龄

      fare : float, # 票价

      embarked : int, # 登船港口 C=1 Q=2 S=3

      ticket_class : int, # 船票类别 1 2 3

      name : str, # 身份 Master Miss Mr Mrs Officer Royalty

      cabin : str, # 船舱号 A-T and U

      family_size : int, # 家庭人数 包含自己

Options:
  -f, --framework [paddle|onnx]  The framework to use for prediction (paddle
                                 or onnx)  [required]
  -m, --model_path TEXT          The path to the model file  [required]
  --help                         Show this message and exit.
```
可以看到,命令行工具详细地输出了这些参数的含义和类型
看参数`-f, --framework` 这个参数填写的是使用的推理框架,填写`paddle`或`onnx`,填写其他的会报错.
看参数`-m, --model_path` 这个参数填写的是模型文件,
如果你是使用onnx的,就要准确到文件名的扩展名,如果你使用的是飞浆,则要不能输入到扩展名
例如`-m models/onnx_model/titan.onnx` **onnx**
还有`-m models/paddle_model/model_titan` **paddle**
我已经将模型文件放在[Titanic/py/models](../../py/models/)下面了

然后我们就可以运行推理
### 进行推理
```bash
# 使用onnx推理
➜  py git:(main) ✗ python ./cli.py predict -f onnx -m models/onnx_model/titan.onnx  1 145 117.5 1 1 Mr U 115 
The passenger can survive.
➜  py git:(main) ✗ python ./cli.py predict -f onnx -m models/onnx_model/titan.onnx  1 845 117.5 1 1 Mr U 1152
The passenger cannot survive.

# 使用飞浆推理
➜  py git:(main) ✗ python ./cli.py predict -f  paddle -m models/paddle_model/model_titan  1 145 117.5 1 1 Mr U 115 
W0830 14:01:14.001946 10242 tensor.cc:399] The `is_initialized` method is deprecated since version 2.3, and will be removed in version 2.4! Please use `initialized` method instead.
I0830 14:01:14.002063 10242 program_interpreter.cc:212] New Executor is Running.
The passenger can survive.
➜  py git:(main) ✗ python ./cli.py predict -f paddle -m models/paddle_model/model_titan 1 845 117.5 1 1 Mr U 1152 
W0830 14:01:18.292855 10366 tensor.cc:399] The `is_initialized` method is deprecated since version 2.3, and will be removed in version 2.4! Please use `initialized` method instead.
I0830 14:01:18.292986 10366 program_interpreter.cc:212] New Executor is Running.
The passenger cannot survive.
```
我们可以看到使用飞浆推理时他会多这些信息,你知道为什么嘛?别看我,我也不知道
推理结果命令行中分别是**The passenger can survive.**和**The passenger cannot survive.**

**The passenger can survive.** 表示存活,而 **The passenger cannot survive.** 表示死亡.

## `runapp`命令
这个命令用于运行flask程序

### 获取帮助信息
```zsh
➜  py git:(main) ✗ python cli.py runapp --help
Usage: cli.py runapp [OPTIONS]

  Run the flask app

Options:
  -f, --framework [paddle|onnx]  The framework to use for prediction (paddle
                                 or onnx)  [required]
  -m, --model_path TEXT          The path to the model file, If it is a model
                                 of flying slurry frame, please enter the file
                                 name, for example,
                                 models/paddle_model/model_titan (if your
                                 model is model_titan.pamodel).  [required]
  --host TEXT                    The host to run the app on  [required]
  --port INTEGER                 The port to run the app on  [required]
  --debug                        Whether to run the app in debug mode
                                 [required]
  --help                         Show this message and exit.
```
其中参数`-f`和`-m`与上文的predict一样.
`--host`参数用于指定flask程序绑定的地址,不填就是`0.0.0.0`;
`--port`参数用于指定绑定的端口,默认`8000`.
`--debug`是一个标志,填写这个标志就代表开启debug模式,不填就是不开启.

感谢你收看本章节内容,当你知道怎么使用这个命令行工具时,就去看下一章吧.
传送门：[flask部署教程](./flaskapp.md)