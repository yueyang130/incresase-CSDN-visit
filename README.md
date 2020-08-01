## 初衷
- 1.增加本人$csdn$访问量（滑稽）
- 2.当作一个$Python$的练手项目
- 3.让更多的人了解到写博客不是为了访客量，而是写出更优质的博客技术文章。（理直气壮）
## 思路 
- 随机$header$ 随机文章访问 随机休息时间 随机$ip$代理
### 关于ip代理池
- 来源
快代理免费高匿代理$ip$：[https://www.kuaidaili.com/free](https://www.kuaidaili.com/free)
- 如何获取
-  > 直接由链接获取$iplist$
- 关于反爬
- >尝试代理$agents$增强反反爬（百度获取）
- [https://yq.aliyun.com/articles/652061](https://yq.aliyun.com/articles/652061)
- ![在这里插入图片描述](https://img-blog.csdnimg.cn/20200205215316561.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L251b3lhbmxp,size_16,color_FFFFFF,t_70)
尝试代理$ip$增强反反爬
### 关于如何访问csdn博客
- 1.$xpath$获取博客数量和访问量
- 2.构造链接用	$requests$,$get$使用随机代理$ip$，随机$header$访问博客
详细见Github：[https://github.com/nuoyanli/Python_csdn](https://github.com/nuoyanli/Python_csdn)
下面放一张没有可视化的运行结果图：![在这里插入图片描述](https://img-blog.csdnimg.cn/20200205215839738.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L251b3lhbmxp,size_16,color_FFFFFF,t_70)
和打包好的exe:
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200205215938412.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L251b3lhbmxp,size_16,color_FFFFFF,t_70)