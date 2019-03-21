#!/Users/jimmy/miniconda3/envs/selenv/bin/python
#coding: utf-8
from webdriverext import ChromeDriverExt 
import time

class XCommand():
    def __init__(self):
        driver = ChromeDriverExt().getInstance()
        def open(cm):
            print("Open: %s" % cm['value'])
            driver.get(cm['value'])
        def add(cm):
            print("Element: object: %s value: %s" % (cm['object'],cm['value']) )
            driver.setElementList(cm)
        def get(cm):
            print("Element: %s" % cm['object'])
        def scroll(cm):
            print("Scroll: %s" % cm['object'])
        def submit(cm):
            print("Submit: %s" % cm['object'])
            (driver.find_element_by_xpath(driver.getElementList(cm))).submit()
        def inj(cm):
            driver.injectText(cm)
        def click(cm):
            print("Click: %s" % cm['object'])
            driver.waitUntilClickable(cm)
        def wait(cm):
            print("Wait: %s" % cm['object'])
            driver.waitUntilElementLocated(cm)
        self.func_list = vars()
    def execute(self,cm):
        self.func_list[cm['ops']](cm)
    def __del__(self):
        self.func_list = None

class app:
    def __init__(self):
        self.list = []
        self.list.append({'ops':'open', 'value':'https://google.com'})
        self.list.append({'ops':'add','object':'search_box','value':'//input[@name="q"]'})
        self.list.append({'ops':'wait','object':'search_box'})
    def run(self):
        driver = ChromeDriverExt().getInstance()
        xc = XCommand()
        for com in self.list:    
            xc.execute(com)
        xc.execute({'ops':'inj','object':'search_box','value':'Hello World'})
        xc.execute({'ops':'submit','object':'search_box'})
        xc.execute({'ops':'wait','object':'search_box'})

if __name__ == "__main__":
    web = ChromeDriverExt().getInstance()
    print(hex(id(web)))
    ap = app()
    ap.run()
    time.sleep(5)
    web.close()
    web.quit()
