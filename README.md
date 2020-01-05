####  URL：
- [Github  URL](https://github.com/liangchuyao/pythonfinalproject)
- [Pythonanywhere  URL](http://liangchuyao.pythonanywhere.com/)

####  HTML文档：
- html使用jinjia2模版语言+html制作。
- 其中模版语言主要使用了循环和判断，用于自动生成表格和翻页按钮。
- 除此之外还通过html的 < select >标签的onchange属性实现了页面刷新，通过< button >标签的onclick属性实现了翻页功能。

####  Python文档：
- python的web部分使用了flask作为后端，选用flask的原因是它轻量化和模块化的特点，适用于页面较少的的web应用。
- 使用了csv库读取保存在csv的数据，然后传递给jinjia2模版引擎渲染图表从而生成页面。

####  Web App动作描述：
- “/”：响应Get请求，返回页面1数据
- “/1”：响应Get请求，返回页面1数据
- “/2”：响应Get请求，返回页面2数据
- “/3”：响应Get请求，返回页面3数据
- “/4”：响应Get请求，返回页面4数据
