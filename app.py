#!/Users/jimmy/miniconda3/envs/selenv/bin/python
#coding: utf-8

import time
import threading
import xml.etree.ElementTree as ET

from webdriverext import ChromeDriverExt 
from seleniumcommand import WebCommand
from eventhandler import EventHandler

class app(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._event = threading.Event()
        self.xc = WebCommand()
        self.list = eh.get_actions() 

    def run(self):
        for c in self.list:
            self.xc.execute(c)

    def pause(self):
        self._event.clear()

    def resume(self):
        self._event.set()

class xmlTemplateParser():
    def __init__(self):
        pass
    def load(self, f):
        e = ET.parse(f)
        root = e.getroot()
        for page in root.find('pages'):
            eh.add_page({'page':page.get('name'),'url':page.get('url')})
            for element in page.find('elements'):
                eh.add_page_element({'page':page.get('name'),'object':element.get('name'),'value':element.text})
        for action in root.find('actions'):
            print(action.get('page'), action.get('element'), action.text)
            eh.add_action({'event':action.text,'page':action.get('page'),'object':action.get('element'),'value':'Hello World'})

eh = EventHandler()

if __name__ == "__main__":
    template = xmlTemplateParser()
    template.load('template.xml')
    web = ChromeDriverExt().getInstance()
    web.set_pages(eh.get_pages())
    print(hex(id(web)))
    ap = app()
    ap.resume()
    ap.start()
    ap.join()
    web.close()
    web.quit()
