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
我们的终端不可能一直挂着,所以我们就需要后台运行.
后台运行的实现在Linux系统上特别简单.

### nohup
这个命令在linux和Mac OS上适用.
命令格式为`nohup command &`.终端关闭后进程任然会继续运行.
```bash
# 来到Titanic/py目录下,运行命令
nohup python app.py & > log.txt # python app.py的输出会定向到log.txt
```
想要关闭就只能杀进程,不知道怎么杀进程就STFW.

### systemctl
这是一个linux的命令行工具,通过使用systemd系统来守护进程.(这种说法可能不太准确)
在一些比较旧的系统中(例如Ubuntu 18)中是使用service命令.
使用这个命令就需要编写一个配置文件,这些配置文件通常位于 `/etc/systemd/system/` 或 `/lib/systemd/system/` 目录中。
以下是一个来自chatGPT和网络的示例(titanic_flask_app.service):
```ini
[Unit]
Description=Titanic Flask App
After=network.target

[Service]
ExecStart=python /path/to/Titanic/py/app.py
Restart=always

[Install]
WantedBy=multi-user.target
```
以下是对这个配置文件的解释(来自:[博客园](https://www.cnblogs.com/zrl66/p/17988380)):
```
　　[Unit]

　　Description：对该服务的描述；
　　Documention：说明文档；
　　Before：在a.service服务启动前，启动本服务；
　　After：在b.target服务组启动后，再启动本服务；
　　Wants：弱依赖于c.service，即使被依赖服务启动失败或停止，本服务仍然运行；
　　Requires：强依赖于d.service，如果被依赖服务启动失败或停止，本服务也会停止。
　　

　　[Service]

　　EnvironmentFile：服务的参数文件，形成$OPTIONS；
　　ExecStart: 服务启动命令
　　ExecReload: 服务重启命令
　　ExecStop: 服务停止命令
　　Type：服务启动类型。默认simple表示ExecStart为主进程，notify类似于simple，启动结束后会发出通知信号。另外还有forking,oneshot,dbus,idle等类型；
　　KillMode：服务停止类型，默认control-group停止时杀死所有子进程，process只杀主进程，none只停止服务，不杀进程；
　　Restart：服务重启类型，默认no不重启，on-success正常退出时重启，on-failure非正常退出时重启，还有always,on-abnormal,on-abort等；
　　RestartSec：间隔多久重启服务。

　　[Install]

　　WantedBy：服务所在的服务组。
```

写完之后将这个文件保存在 `/etc/systemd/system/` 或 `/lib/systemd/system/` 目录中.
终端运行
```bash
sudo systemctl systemctl daemon-reload
sudo systemctl start titanic_flask_app.service # 你保存时的文件名
# 停止服务：sudo systemctl stop titanic_flask_app.service
# 检查状态: sudo systemctl status titanic_flask_app.service
```

### Windows上的后台运行
在Windows上可以使用start命令(PowerShell的Start-Process),其余的方法请自行上网.

### 宝塔部署
使用宝塔面板可以部署python项目,只要在宝塔安装python版本,添加项目就可以直接运行

### docker部署
使用docker也可以很好地后台运行,后面会出相关教程

## 一些问题
在我们使用flask的时候会看见弹出一个提示,大概是叫我们使用WSGI服务器,
大家可以自行上网找教程,经典地有uwsgi(只适用于linux).

感谢你收看本章节内容,看到这里,你已经离成功更进一步啦,请移步下一章.
传送门：[vue部署教程](./vue.md)