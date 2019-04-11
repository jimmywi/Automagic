#!/Users/jimmy/miniconda3/envs/selenv/bin/python
#coding: utf-8
import threading
from webdriverext import ChromeDriverExt 
from seleniumcommand import WebCommand
import csv
import time
import xml.etree.ElementTree as ET

class app(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._event = threading.Event()
        self.xc = WebCommand()
        self.list = []
        self.list.append({'page':'overview','event':'open','object':'null','value':'null'})
        self.list.append({'page':'overview','event':'inject','object':'searchbox','value':'Hello World'})
        self.list.append({'page':'overview','event':'submit','object':'searchbox','value':'null'})
        self.list.append({'page':'services','event':'open','object':'null','value':'null'})

    def run(self):
        for cm in self.list:
            self._event.wait()
            self.xc.execute(cm)

    def pause(self):
        self._event.clear()

    def resume(self):
        self._event.set()

class xmlTemplateParser():
    def __init__(self):
        self.xc = WebCommand()
    def load(self, f):
        e = ET.parse(f)
        root = e.getroot()
        for page in root.find('pages'):
            print(page.get('name'))
            self.xc.execute({'event':'addpage','page':page.get('name'),'url':page.get('url')})
            for element in page.find('elements'):
                print("- %s: %s: %s" % (page.get('name'), element.get('name'), element.text))
                self.xc.execute({'page':page.get('name'),'event':'addelement','object':element.get('name'),'value':element.text})

if __name__ == "__main__":
    template = xmlTemplateParser()
    template.load('template.xml')
    web = ChromeDriverExt().getInstance()
    print(hex(id(web)))
    ap = app()
    ap.resume()
    ap.start()
    ap.join()
    time.sleep(5)
    web.close()
    web.quit()
