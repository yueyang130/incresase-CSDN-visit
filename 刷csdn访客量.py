# -*- coding: utf-8 -*-
'''
@Time    : 2019/10/30 16:17
@Author  : nuoyanli
@Site    :
@File    : csdn访客量.py
@Software: vscode
'''
# 思路 随机header 随机文章访问 随机休息时间
# 导入相关爬虫库和解析xml库即可

"""
Annotation by Yue Yang:
1. note: when use requests.get(), please use headers, else probably get nothing from the target url.

2. the code is modified by Yue Yang. The changes are following(see details in git):
    a. the split-page method now dosn't work, so we adapt a not split-page method.
    b. we change from sleeping a fixed time to sleep a random time, which is more like the real visit.

3. note that we use some proxies which comes from  'https://www.kuaidaili.com/free/inha/'
    sometimes we may fail to visit the web, please try again. 
    sleeping before visit the proxy-get web again can reduce the risk of failure.
"""

import linecache
import time
import re
from pyquery import PyQuery as pq
import requests
from bs4 import BeautifulSoup
import random
from fake_useragent import UserAgent
from lxml import etree
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }

# 爬取csdn类


class ScrapyMyCSDN:
    ''' class for csdn'''

    def __init__(self, blogname):
        '''init 类似于构造函数 param[in]:blogname:博客名'''
        csdn_url = 'https://blog.csdn.net/'  # 常规csdnurl
        self.blogurl = csdn_url + blogname  # 拼接字符串成需要爬取的主页url
        self.blog_nums = 0  # 原创博客数量
        self.blog_vs = 0  # 博客访客量

    '''博客访问量'''

    def get_vs(self, headers, proxies):
        main_response = requests.get(
            self.blogurl, timeout=10, headers=headers, proxies=proxies)
        if main_response.status_code == 200:
            print('获取成功')
            htm = etree.HTML(main_response.content.decode('utf-8'))
            rep = str(htm.xpath(
                "//*[@id='asideProfile']/div[2]/dl[5]/@title"))
            rep = rep.replace('[\'', '')
            self.blog_vs = int(rep.replace('\']', ''))
            return self.blog_vs  # 返回博文数量
        else:
            print('爬取失败')
            return 0  # 返回0 说明博文数为0或者爬取失败

    ''' Func:获取写了多少篇原创文章 '''
    ''' return:写了多少篇原创文章'''

    def getOriginalArticalNums(self, headers, proxies, fal):
        main_response = requests.get(
            self.blogurl, timeout=10, headers=headers, proxies=proxies)
        # 判断是否成功获取 (根据状态码来判断)
        # print('状态码', main_response.status_code)
        if main_response.status_code == 200:
            if fal:
                print('获取成功')
            self.main_html = main_response.text
            # print(self.main_html, main_response.text)
            html = BeautifulSoup(self.main_html, "html.parser")
            # print('html', html)
            # print('内容', html.find_all('div', class_='data-info d-flex item-tiling'))
            for tag in html.find_all('div', class_='data-info d-flex item-tiling'):
                # print('tag', tag)
                self.blog_nums = int(
                    tag.find('span', class_='count').get_text())
                break
                # print('blog_nums', self.blog_nums)
            if fal:
                print("原创博客数量为"+":"+str(self.blog_nums))
            return self.blog_nums  # 返回博文数量
        else:
            if fal:
                print('爬取失败')
            return 0  # 返回0 说明博文数为0或者爬取失败

    ''' Func：分页'''
    ''' param[in]:nums:博文数 '''
    ''' return: 需要爬取的页数'''

    def getScrapyPageNums(self, nums, fal):
        self.blog_original_nums = nums
        if nums == 0:
            if fal:
                print('它没写文章，0页啊！')
            return 0
        else:
            if fal:
                print('现在开始计算')
            cur_blog = nums/20  # 获得精确的页码
            cur_read_page = int(nums/20)  # 保留整数
            # 进行比对
            if cur_blog > cur_read_page:
                self.blog_original_nums = cur_read_page + 1
                if fal:
                    print('你需要爬取 %d' % self.blog_original_nums + '页')
                return self.blog_original_nums  # 返回的数字
            else:
                self.blog_original_nums = cur_read_page
                if fal:
                    print('你需要爬取 %d' % self.blog_original_nums + '页')
            return self.blog_original_nums

    '''Func:开始爬取，实际就是刷浏览量hhh'''
    '''param[in]:page_num:需要爬取的页数'''
    '''return:0:浏览量刷失败'''

    def beginToScrapy(self, page_num, header, proxies, fal):
        if page_num == 0:
            if fal:
                print('连原创博客都不写 爬个鬼!')
            return 0
        else:
            article_doc = requests.get(
                self.blogurl, timeout=10, headers=header, proxies=proxies)  # 访问该网站
            # 先判断是否成功访问
            if article_doc.status_code == 200:

                # 进行解析
                cur_page_html = article_doc.text
                # print(cur_page_html)
                soup = BeautifulSoup(cur_page_html, 'html.parser')
                articles = soup.find_all('p', class_="content")
                for link in articles:
                    # print(link.find('a')['href'])
                    art_url = link.find('a')['href']
                    requests.get(art_url, proxies=proxies, headers=header)  # 进行访问
                    time.sleep(0.1)
            else:
                if fal:
                    print('访问失败')
        if fal:
            print('访问结束')


class get_kuaidaili_ip():   # 获取快代理免费代理ip
    # 尝试代理agents增强反反爬
    def random_agent(self):
        user_agents = [
            "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
            "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
            "MQQBrowser/25 (Linux; U; 2.3.3; zh-cn; HTC Desire S Build/GRI40;480*800)",
            "Mozilla/5.0 (Linux; U; Android 2.3.3; zh-cn; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
            "Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaE75-1 /110.48.125 Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413"
            'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
            'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11'
        ]
        return random.choice(user_agents)
    # 尝试代理IP增强反反爬

    def get_ip_list(self, url, headers, proxies):
        web_data = requests.get(url, headers=headers, proxies=proxies)
        soup = BeautifulSoup(web_data.text, 'lxml')
        ips = soup.find_all('tr')
        ip_list = []
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            ip_list.append(tds[0].text + ':' + tds[1].text)
        return ip_list

    def get_random_ip(self, ip_list):
        proxy_list = []
        for ip in ip_list:
            proxy_list.append('http://' + ip)
        proxy_ip = random.choice(proxy_list)
        proxies = {'http': proxy_ip}
        return proxies

    def get_one(self, proxies = None):
        #url = 'http://www.xicidaili.com/nn/5'
        url = 'https://www.kuaidaili.com/free/inha/%s/' % random.randint(1, 10)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }
        ip_list = self.get_ip_list(url, headers=headers, proxies=proxies)
        # print(ip_list)
        return self.get_random_ip(ip_list)


def run_(name_, su_):
    for i in range(1, 2):

        url = get_kuaidaili_ip()
        proxies = url.get_one()
        # print("使用的代理ip为：", proxies)
        # 如何调用该类
        mycsdn = ScrapyMyCSDN(name_)  # 初始化类 参数为博客名
        # print("初始访客量为"+":"+str(vs_0))
        cur_write_nums = mycsdn.getOriginalArticalNums(
            headers, proxies, False)  # 得到写了多少篇文章

        cur_blog_page = mycsdn.getScrapyPageNums(
            cur_write_nums, False)  # cur_blog_page:返回需要爬取的页数
        mycsdn.beginToScrapy(cur_blog_page, headers, proxies, False)
        time.sleep(random.random() * 0.1)  # 给它休息时间 还是怕被封号的


def run():
    name_ = input("请输入您的csdn博客id:")
    su_ = int(input("请输入您要刷的次数(这里的次数指博主您所有博客的访问次数，请注意我们只刷原创博客哦，支持原创！！！):"))
    while su_ >= 10000:
        print("刷访客量的行为可不好哦，请不要太贪心！！(号被封了可别哭)")
        su_ = int(input("请输入您要刷的次数(这里的次数指博主您所有博客的访问次数，请注意我们只刷原创博客哦，支持原创！！！):"))
    mycsdn = ScrapyMyCSDN(name_)

    print("正在计算访客量，请勿关闭.......")
    #run_('nuoyanli', su_)  # 嘻嘻用我的代码就帮我也刷一下吧(据说好人一般都会取消这个注释)
    url = get_kuaidaili_ip()
    proxies = url.get_one()
    vs = mycsdn.get_vs(headers, proxies=proxies)
    time.sleep(5)
    failCnt = 0

    for i in range(1, su_+1):
        print(f'{i} / {su_}')
        try:
            new_proxies = url.get_one(proxies)
            proxies = new_proxies
            failCnt = 0
        except IndexError:
            time.sleep(5)
            failCnt += 1
            if failCnt > 10:
                print('已经连续十次获取新代理失败，害怕被封号，所以停了')
                raise Exception


        print("使用的代理ip为：", proxies)
        # 如何调用该类
        try:
            vs_0 = mycsdn.get_vs(headers, proxies)  # 初始访客量
            print("初始访客量为"+":"+str(vs_0))
            cur_write_nums = mycsdn.getOriginalArticalNums(
                headers, proxies, False)  # 得到写了多少篇文章
            cur_blog_page = mycsdn.getScrapyPageNums(
                cur_write_nums, False)  # cur_blog_page:返回需要爬取的页数
            mycsdn.beginToScrapy(cur_blog_page, headers, proxies, False)
        except requests.exceptions:
            pass

        time.sleep(random.random())  # 给它休息时间 还是怕被封号的
    vs_1 = mycsdn.get_vs(headers, proxies)  # 刷后的访客量
    print("刷后的访客量"+":"+str(vs_1), end='')
    print(",增加了" + str(vs_1 - vs) + "的访客量")
    if vs_1 - vs > 0:
        print("哇有人悄悄访问了你的博客呢，快去看看是谁吧！")


if __name__ == '__main__':
    run()
