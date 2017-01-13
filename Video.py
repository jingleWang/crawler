class video:

    def __init__(self):
        self._id = -1
        self._name = ""
        self._category = ""
        self._intro = "1"
        self._time = ""
        self._downloads = []

    def setID(self,id):
        self._id = id
        return

    def setName(self,name):
        self._name = name
        return

    def setCategory(self,category):
        self._category = category
        return

    def setIntro(self,intro):
        self._intro = intro
        return

    def setTime(self,time):
        self._time = time
        return

    def setDownloads(self,name,url,passwd):
        self._downloads.append({'name':name,'url':url,'passwd':passwd})
        return

    def getID(self):
        return self._id

    def getName(self):
        return self._name

    def getCategory(self):
        return self._category

    def getIntro(self):
        return self._intro

    def getTime(self):
        return self._time

    def getDownloadsList(self):
        return self._downloads

    def getDownloadsStr(self):
        str = ""
        for video in self._downloads:
            str += "name: "+video['name']+\
                   "\nurl: "+video['url']+\
                    "\npassword: "+video['passwd']+"\n\n"

        return str

    def toString(self):
        return "name: "+self._name+"   id:" + self._id+"   category: " +\
               self._category+"   time :"+self._time+"   intro: "+self._intro +\
            "   downloads: " + self.getDownloadsStr() + "\n"


