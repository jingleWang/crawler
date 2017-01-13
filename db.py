import pymysql


class db:

    __username = ""
    __host = ""
    __db = ""
    __pass = ""

    __video = []



    def connect(self):
        self.__connection = pymysql.connect(self.__host, self.__username, self.__pass, self.__db)
        self.__connection.set_charset('utf8')
        self.__cursor = self.__connection.cursor()

    def close(self):
        self.__connection.close()


    def addVideo(self,video):
        self.__video.append({
            'name':video.getName(),
            'id':video.getID(),
            'category':video.getCategory(),
            'intro':video.getIntro(),
            'time':video.getTime(),
            'baidu':video.getDownloadsStr()
        })

    def update(self):

        self.connect()

        self.__updateVideos()

        self.__connection.commit()
        print('update to database')
        self.close()


    def __updateVideos(self):


        for v in self.__video:
            insert = "insert into resources values(%(id)s,%(time)s,%(category)s,%(name)s,%(intro)s,%(baidu)s)"
                  # (v['id'],v['time'],v['category'],v['name'],v['intro'],v['baidu'])

            update = "update resources set update_time=%(time)s,downloads=%(baidu)s where id = %(id)s"
                     # (v['time'],v['baidu'],v['id'])

            if self.__isExist(v['id']):
                # print(update)
                self.__cursor.execute(update,v)
            else:
                # print(insert)
                self.__cursor.execute(insert,v)

        self.__video.clear()

    def __isExist(self,id):
        sql = "select * from resources where id = '%s'" % (id)
        self.__cursor.execute(sql)

        return len(self.__cursor.fetchall())>0


