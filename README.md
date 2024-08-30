<h1 align="center">Titanic</h1>
你能在泰坦尼克号上存活吗？
Could you survive on the Titanic?

## 作者 Author
作者(Anthor): Sen
邮箱(Email): tianhuzong@qq.com
github: [tianhuzong](https://github.com/tianhuzong)
gitee: [gitee](https://gitee.com/thzsen)

---
[English Version](#english-version)

## 项目

预测如果你在在泰坦尼克号上能否存活？模型训练代码采用paddle框架编写，并编写了一个vue的前端界面。

## 许可证
MIT许可证 [License](LICENSE)

版权 (c) 2024 Sen

兹免费授权任何人获得本软件和相关文档文件（“软件”），在软件的使用、复制、修改、合并、出版、分发、再授权和/或销售的过程中，无限制地使用该软件，只要满足以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或重要部分中。

软件按“原样”提供，不附有任何形式的明示或暗示的担保，包括但不限于适销性、特定用途的适用性和不侵权的担保。在任何情况下，作者或版权持有人均不对因软件或软件的使用或其他交易而引起的任何索赔、损害或其他责任承担责任，无论是合同诉讼、侵权行为或其他诉讼形式。

## 免责声明

本项目可供学习研究使用，允许商用。
使用本项目请准守开源协议和相关法律法规。
请勿用于任何非法用途，否则后果自负，本人不承担任何责任，技术无罪。

## 项目结构
```
Titanic/
    |--- docs/ //文档
    |--- py/ //py代码
        |--- data/ //训练数据集
        |--- models/ //模型文件
            |--- paddle_model/ //飞浆模型文件目录
            |--- paddlejs_model/ //paddle.js模型文件目录
            |--- onnx_model/ //onnx模型目录
        |--- trainer/ //包含训练和推理的脚本
        |--- app.py //flask程序
        |--- cli.py //命令行工具
        |--- requirements.txt //依赖包文件
   |--- vue/ //前端代码
        |--- titan_web/
            |--- *.json/index.html ... //这些都是vue的文件
            |--- src/ //存放着源代码
            |--- public/ //存放着一些视频文件之类的
   |--- //以下放置开源协议和自述文件
```

## 文档
[查看文档](docs/)

## English Version

## Project
Predict if you can survive on the Titanic? The model training code is written in paddle framework, and a front-end interface of vue is written.

## License
MIT License[License](LICENSE)

Copyright (c) 2024 仙

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## disclaimer

This project is available for educational and research purposes and is allowed for commercial use.

Please comply with the open source license and relevant laws and regulations when using this project.

Do not use this project for any illegal purposes. Otherwise, you will be held responsible for any consequences, and I will not assume any liability. Technology is not guilty.

## Project structure

```
Titanic/
    |--- docs/ //document
    |--- py/ //python source code
        |--- data/ //train datasets
        |--- models/ //model files
            |--- paddle_model/ //paddlepaddle model files
            |--- paddlejs_model/ //paddle.js model files
            |--- onnx_model/ //onnx model files
        |--- trainer/ //including training and reasoning scripts
        |--- app.py //flask program
        |--- cli.py //CLI
        |--- requirements.txt 
   |--- vue/ //Front-end code
        |--- titan_web/
            |--- *.json/index.html ... //
            |--- src/ //source codes
            |--- public/ //There are some video files and so on.
   |--- //Readme and License
```

## document
[document](docs/)