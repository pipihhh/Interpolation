# Interpolation
基于python实现一个拉格朗日插值、牛顿插值、Hermit插值图形的web项目

安完所需要的依赖后且配置好core.py行首的数据库配置后 直接运行core.py即可
页面的右上角为添加曲线。页面的曲线图的右侧为下载图片
页面下拉为各式算法的简介等
静态文件的url为/assets/img/{filename.png}
下载文件的url为/download/{filename.png} 为了减少重复计算 为每次的计算结果做了数据库的缓存
