from spider import spider
import timeit

timer = timeit.Timer("process()",'from __main__ import process')


def process():
    print("-----start-----")
    url = "http://huhupan.com/dsj/"
    s = spider(url)
    s.setDepth(1)
    s.run()


print("totally use " ,timer.timeit(1)," seconds")
print("-----end-----")
