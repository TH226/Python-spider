# coding:utf8
from baike_page import url_manager, html_download, html_parser, html_output

class SpiderMain(object):
    def __init__(self):   #初始化
        self.urls = url_manager.UrlManager()
        self.downloader = html_download.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_output.HtmlOutputer()
    
    def craw(self, root_url):  #抓取网页
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():  #判断是否有新的网页抓取
            try:
                new_url = self.urls.get_new_url() #获取新的url
                print "craw %d : %s"%(count,new_url)
                html_cont = self.downloader.download(new_url)#获取新网页的链接
                new_urls,new_data=self.parser.parse(new_url,html_cont)  #解析网址和网址内容
                self.urls.add_new_urls(new_urls) #url放入管理器
                self.outputer.collect_data(new_data) #网页数据收集
                if count == 30:
                    break
                count +=1
            except:
                print 'craw failed'
        self.outputer.output_html()



if __name__=="__main__":
    root_url="http://baike.baidu.com/item/Python" 
    obj_spider = SpiderMain() 
    obj_spider.craw(root_url) 
    
    
    
     