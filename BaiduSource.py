import urllib.request as http
import re
class BaiduSource:
    def __init__(self,video):
        self.video = video

    INTERFACE = "http://huhupan.com/e/extend/down/?id="

    __list_express = "<div class=\"box\">(.*?)<div class=\"box4 kkk\">"
    __list_pattern = re.compile(__list_express,re.S)

    __t1_express = "<div class=\"box2\">(.*?)<script>"
    __t1_pattern = re.compile(__t1_express,re.S)

    __info_express = "href=\"([^\"]*)\">(.*?)</a>(.*)value=\"([^\"]*)\""
    __info_pattern = re.compile(__info_express,re.S)


    @staticmethod
    def getPAGE(id):
        try:
            html = http.urlopen(BaiduSource.INTERFACE+id).read().decode('utf-8')
            return html
        except:
            return False

    @staticmethod
    def getResources(html):

        resources = []
        list = BaiduSource.__list_pattern.search(html)
        if not list:
            return resources

        m = BaiduSource.__t1_pattern.findall(list.group(1))
        if not m:
            return resources

        for s in m:
            info = BaiduSource.__info_pattern.search(s)
            if not info:
                continue

            resources.append({"name":info.group(2),
                              "url":info.group(1),
                              "passwd":info.group(4)})
        return resources

    def get(self):
        id = self.video.getID()
        page = self.getPAGE(id)
        if not page:
            print("can't get the resourece of ",self.video.getName())
            return

        for info in self.getResources(page):
            self.video.setDownloads(info['name'],info['url'],info['passwd'])






