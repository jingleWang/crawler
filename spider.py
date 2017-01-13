import urllib.request as http
from BaiduSource import BaiduSource as bd
import gevent.monkey
from db import db

from parsers import parser

class spider:

    def __init__(self,entrance=""):
        try:
            self.__entrance = entrance
            http.urlopen(entrance)
            self.__entranceIsOK = True
            self.__videos = []
            self.__depth = 0
            self.__total = 0
            self.db = db()
        except:
            self.__entranceIsOK = False

    def getHtml(self,url):
        try:
            page = http.urlopen(url)
            html = page.read().decode('utf-8')
            return html
        except:
            print("Can't visit site: " + self.__entrance)
            self.__statistics()

    def setDepth(self,depth):
        self.__depth = depth


    def run(self):
        if self.__entranceIsOK:
            self.__counter = 0
            self.__videos = []
            nextPage = self.__entrance
            while True:
                print("The No." + str(self.__counter + 1) + " page")
                page = self.getHtml(nextPage)

                print("GET PAGE\nSTART PARSING")
                p = parser(page)
                self.__videos.extend(p.getVideos())

                print("GET " + str(len(p.getVideos())) + " VIDEOS\n\n")
                nextPage = p.getNextPage()

                print("----start get baidu resources----")
                self.__getBaiduResources()

                self.__total+=len(self.__videos)
                self.__videos.clear()
                print("----already fetch all of this page----")

                self.db.update()

                self.__counter += 1
                if self.__depth != 0 and self.__counter >= self.__depth:
                    self.__statistics()
                    break
                elif not nextPage:
                    self.__statistics()
                    break
        else:
            print("FAIL To Run,url:"+self.__entrance+" can't be visited")

    def __process(self,v):
        s = bd(v)
        s.get()
        self.db.addVideo(v)
        # print(v.toString())

    def __getBaiduResources(self):
        thread = []

        for v in self.__videos:
            thread.append(gevent.spawn(self.__process,v))

        gevent.joinall(thread)

    def getVideos(self):
        return self.__videos


    def __statistics(self):
        print("----statistics----")
        print("Visit ",self.__counter," pages")
        print("Find ",self.__total," videos")




