import re
from Video import video
class parser:
    '''
    解析html
    '''
    __main_express = '<div class=\"main\">(((?!class=\"sider\").)*)</div>'
    __main_pattern = re.compile(__main_express, re.S)

    __video_express = '<div class=\"block\">(((?!block).)*)</div>';
    __video_pattern = re.compile(__video_express, re.S)

    __idAndname_express = "<a href=\"([^\"]*)\"  target=\"_ablank\" > (.*) </a>"
    __idAndname_pattern = re.compile(__idAndname_express)

    __category_express = "rel=\"category tag\" >([^<]*)</a>"
    __category_pattern = re.compile(__category_express)

    __time_express = "<span><i class=\"fa fa-clock-o\"></i> ([^<]*) </span>"
    __time_pattern = re.compile(__time_express)

    __id_express = "([0-9]+)\.html"
    __id_pattern = re.compile(__id_express)

    __intro_express = " <div class=\"preview\">(((?!div).)*)</div>"
    __intro_pattern = re.compile(__intro_express,re.S)

    __nextPage_express = "<a href=\"([^>]*)\">下一页</a>"
    __nextPage_pattern = re.compile(__nextPage_express)

    def __init__(self,html):
        if html:
            self.html = html
            self.noErr = True
            self.videos = []

            self.__getTVList()
            self.__getTVsDetail()


    def __getTVList(self):
        """
        获得视频列表
        :param html:
        :return:
        """
        if self.noErr:
            m = parser.__main_pattern.search(self.html)
            if m.group(1):
                self.noErr = True
                self.TVList = m.group(1)
        else:
            pass


    def __getVideoIDandName(self,str):
        '''
        获得视频id 和 名称
        :param str:
        :return: ID,NAME
        '''

        data = parser.__idAndname_pattern.search(str)
        if data:
            url = data.group(1)
            name = data.group(2)
            data = parser.__id_pattern.search(url)
            if data:
                return data.group(1), name


    def __getVideoCategory(self,str):

        data = parser.__category_pattern.search(str)
        if data:
            return data.group(1)

    def __getVideoUpdateTime(self,str):

        data = parser.__time_pattern.search(str)
        if data:
            return data.group(1)

    def __getVideoInfo(self,str):
        data = parser.__intro_pattern.search(str)
        if data:
            return data.group(1)
        else:
            return "no introduce"

    def __getTVsDetail(self):
        '''
        从视频列表中返回视频集合
        :param html:
        :return:
        '''
        if self.noErr:

            videos = parser.__video_pattern.findall(self.TVList)
            for  v in videos:
                videoDetail = video()
                id,name = self.__getVideoIDandName(v[0])
                category = self.__getVideoCategory(v[0])
                time = self.__getVideoUpdateTime(v[0])
                intro = self.__getVideoInfo(v[0])

                videoDetail.setID(id)
                videoDetail.setName(name)
                videoDetail.setTime(time)
                videoDetail.setCategory(category)
                videoDetail.setIntro(intro)
                self.videos.append(videoDetail)
        else:
            return False

    def getVideos(self):
        return self.videos

    def getNextPage(self):
        data = parser.__nextPage_pattern.search(self.TVList)
        if data:
            return data.group(1)
        else:
            return False