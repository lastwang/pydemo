#coding:utf-8
import urllib2
#import requests
class HtmlDownload(object):
    def download(self,url):
        if url is None:
            return None
        response=urllib2.urlopen(url)
        if response.getcode()!=200:
            return  None
        return response.read()
    # def download(self, url):
    #     if url is None:
    #         return  None
    #     response=requests.get(url)
    #     if response.status_code!=200:
    #         return None
    #     return  response.text
