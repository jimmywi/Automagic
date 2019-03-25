#!/Users/jimmy/miniconda3/envs/selenv/bin/python
#coding: utf-8
import threading
from webdriverext import ChromeDriverExt 
from seleniumcommand import WebCommand
import csv
import time

class app(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._event = threading.Event()
        #f = open('template.csv', 'r')
        self.xc = WebCommand()
        self.list = []
        self.list.append({'ops':'open', 'value':'https://google.com'})
        self.list.append({'ops':'add','object':'search_box','value':'//input[@name="q"]'})
        self.list.append({'ops':'wait','object':'search_box'})
        self.list.append({'ops':'inj','object':'search_box','value':'Hello World'})
        self.list.append({'ops':'submit','object':'search_box'})
        self.list.append({'ops':'wait','object':'search_box'})

    def run(self):
        for cm in self.list:
            self._event.wait()
            self.xc.execute(cm)

    def pause(self):
        self._event.clear()

    def resume(self):
        self._event.set()

if __name__ == "__main__":
    web = ChromeDriverExt().getInstance()
    print(hex(id(web)))
    ap = app()
    ap.resume()
    ap.start()
    time.sleep(1)
    ap.pause()
    time.sleep(5)
    ap.resume()
    ap.join()
    time.sleep(5)
    web.close()
    web.quit()
