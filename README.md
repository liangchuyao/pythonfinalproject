# Python Final Project
***
####  URL：
- [Github  URL](https://github.com/liangchuyao/pythonfinalproject)
- [Pythonanywhere  URL](http://liangchuyao.pythonanywhere.com/)
####  项目介绍：
 * 项目共有4个url。
 * 第一个url是主界面，里面有简要的项目开篇介绍，放了3张世界各国分布地图，以颜色来区分世界的GDP、森林覆盖率、PM2.5空气污染指数，并通过一个选择下拉框将3个地图放在一起，较为美观并方便选择。下面有一个地区选择的下拉框，还有一个实现跳转功能的按钮。除此之外还有读取flask.csv后的内容，形成一个表格，有CountryName，Indicator Name，Year和Value三个模块。
 * 第二个url是在第一个界面点击“下一页”跳转按钮后跳转的页面。上方有关于项目推导后的文字介绍，有一个2010年和2016年PM2.5排放变化的柱形图，下面有一个年份选择的下拉框，还有一个实现跳转功能的按钮。
 * 第三个url是在第二个界面点击“下一页”跳转按钮后跳转的页面。上方有关于项目推导后的文字介绍，放了3张折线图，来区分世界的GDP、森林覆盖率、PM2.5空气污染指数，并通过一个选择下拉框将3个地图放在一起。下面有一个地区选择的下拉框，还有一个实现跳转功能的按钮。
 * 第四个url是在第三个界面点击“下一页”跳转按钮后跳转的页面。上方有关于项目推导后的文字介绍，放了1个条形图和1个折线图对比，是关于各国每年人均GDP和PM2.5空气污染指数。下面有一个地区选择的下拉框，还有一个实现跳转功能的按钮。
******
###  HTML文档：
- html使用jinjia2模版语言+html制作。
- 其中模版语言主要使用了循环和判断，用于自动生成表格和翻页按钮。
- 除此之外还通过html的 < select >标签的onchange属性实现了页面刷新，通过< button >标签的onclick属性实现了翻页功能。
- 用.dataframe{width:100%;}实现表格全局布满。

###  Python文档：
- python的web部分使用了flask作为后端，选用flask的原因是它轻量化和模块化的特点，适用于页面较少的的web应用。
- 使用了csv库读取保存在csv的数据，然后传递给jinjia2模版引擎渲染图表从而生成页面。
- 通过flask "/"路由，指定GET请求方法，读取flask.csv 文件数据内容 并以result.html文件作为模板以响应返回。
- 通过 "/hurun"路由，指定POST请求方式， 调用函数将结果返回前段界面。
- 选取pandas模块，利用df1 = pd.read_csv("", encoding='')读取flask.csv
- line_markpoint: 传入 select_nation.csv 数据对象，生成折线图，sn列内容作为x轴数据，money列和dependency列数据作为y轴数据.

###  Web App动作描述：
- “/”：响应Get请求，返回页面1数据
- “/1”：响应Get请求，返回页面1数据
- “/2”：响应Get请求，返回页面2数据
- “/3”：响应Get请求，返回页面3数据
- “/4”：响应Get请求，返回页面4数据
