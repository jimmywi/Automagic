#!/Users/jimmy/miniconda3/envs/selenv/bin/python
#coding: utf-8
from webdriverext import ChromeDriverExt 
import time

class XCommand():
    def __init__(self):
        driver = ChromeDriverExt().getInstance()
        def open(cm):
            print("Open: %s" % cm['input'])
            driver.get(cm['input'])
        def path(cm):
            print("Path: %s" % cm['input'])
        def textbox(cm):
            print("Textbox: %s" % cm['input'])
        def getelems(cm):
            print("Elements: %s" % cm['input'])
        def getelem(cm):
            print("Element: %s" % cm['input'])
        def scroll(cm):
            print("Scroll: %s" % cm['input'])
        def submit(cm):
            print("Submit: %s" % cm['input'])
        def click(cm):
            print("Click: %s" % cm['input'])
            driver.waitUntilClickable(cm['input'])
        def wait(cm):
            print("Wait: %s" % cm['input'])
            driver.waitUntilElementLocated(cm['input'])
        self.func_list = vars()
    def execute(self,cm):
        self.func_list[cm['type']](cm)
    def __del__(self):
        self.func_list = None

class app:
    def __init__(self):
        self.list = []
        self.list.append({'type':'open', 'input':'https://google.com'})
        self.list.append({'type':'wait','input':'q'})
    def run(self):
        driver = ChromeDriverExt().getInstance()
        xc = XCommand()
        for com in self.list:    
            xc.execute(com)
        search_box = driver.find_element_by_name('q')
        search_box.send_keys('Apple Pie')
        search_box.submit()
        xc.execute({'type':'wait','input':'q'})

if __name__ == "__main__":
    web = ChromeDriverExt().getInstance()
    print(hex(id(web)))
    ap = app()
    ap.run()
    time.sleep(5)
    web.close()
    web.quit()
