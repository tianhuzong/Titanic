<h1 align="center">前端代码教程</h1>

本章节我们介绍前端代码的部署
vue的部署方法其实也就那样,我们就简单讲一下吧.

## 命令行运行
进入项目根目录,然后`cd vue/titan`,然后运行
```bash
npm run dev
```
然后等待输出就可以访问了,默认绑定地址`http://localhost:5173`

## 编译项目
```bash
# 进入项目根目录,然后`cd vue/titan`,然后运行
npm run build
# 编译完成后进入dist项目
cd dist
# 下面有一个index.html文件,是这个项目的主文件
# 我们可以直接使用node的httpserver
# 如果没有安装httpserver请先安装
# npm install httpserver
httpserver

# 或使用python的http.server
python -m http.server --bind 0.0.0.0 8000
```
也可以将编译完的文件上传到一些静态网站托管的例如github page.

我们可以来看看`vue/titan_web/src`目录几个主要的文件.
- `main.js`,`index.html`,`style.css`,`App.vue` 由vite生产的几个文件.
- `utils.js` 用于请求后端预测结果的接口.
- `useVideoPlayer.js` 预测结果播放动画控制接口.
- `Gate.vue` 将其他文件整合到一个页面的.
- `Main.vue` 编写预测的字段输入框的主窗口.
- `VideoPlayer.vue` 播放器的界面.

**由于我使用`onnxruntime`一直异常,并且`paddlejs`我找不到很好的解决方案,所以我决定使用前后端分离**
**如果您有什么办法解决的话可以编写后提交PR**

如果您找到了什么实现方法,请在`vue/titan_web/src/utils.js`提供一个`predict`接口
以下是个例子:
```js
export function predict(
    sex, // 男1 女0
    age, // 年龄
    fare, // 票价
    embarked, // 登船港口 C=1 Q=2 S=3
    ticketClass, // 船票类别 1 2 3
    name, // 身份 Master Miss Mr Mrs Officer Royalty
    cabin, // 船舱号 A-T and U
    familySize // 家庭人数 包含自己
){
    //请求结果
    var result = request_result(...);
    //返回格式 {result: true}或{result: false}
    return result
}
```

前端代码的部署教程就到这里,下一章节是对于训练模型代码的一些讲解,可以选择性地阅读.
传送门:[训练教程](./train.md)