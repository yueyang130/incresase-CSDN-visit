## 说明
1.本代码的大部分内容都是来自仓库https://www.kuaidaili.com/free/inha/ ， 笔者一开始只是想找一个能刷CSDN访客量的现成代码。但是现有代码大部分都失效了，因此在现有代码基础上做了改进。改进部分在和注意事项都写在了.py文件开头的annotation部分。

2.关于使用到的爬虫技术，本人写了一篇简短的博客，详见https://blog.csdn.net/qq_43714612/article/details/107738366

3.使用方法



### 关于如何访问csdn博客
- 1.$xpath$获取博客数量和访问量
- 2.构造链接用	$requests$,$get$使用随机代理$ip$，随机$header$访问博客
详细见Github：[https://github.com/nuoyanli/Python_csdn](https://github.com/nuoyanli/Python_csdn)
下面放一张没有可视化的运行结果图：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200205215839738.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L251b3lhbmxp,size_16,color_FFFFFF,t_70)
和打包好的exe:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200205215938412.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L251b3lhbmxp,size_16,color_FFFFFF,t_70)