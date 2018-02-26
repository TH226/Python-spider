# coding:utf8
import urllib2

class HtmlDownloader(object):
    
    
    
    def download(self,url):  #使用urllib2获取网页链接
        if url is None:
            return None
        response = urllib2.urlopen(url)
        
        if response.getcode()!=200: #判断请求是否成功
            return None
        return response.read()



