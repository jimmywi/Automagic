from webdriverext import ChromeDriverExt

class WebCommand():
    def __init__(self):
        driver = ChromeDriverExt().getInstance()
        def addevent(cm):
            driver.add_events(cm)
        def getevent(cm):
            return driver.get_events()
        def open(cm):
            print("Open: %s" % cm['page'])
            driver.get(driver.get_page(cm))
        def addpage(cm):
            print("Page: %s" % (cm['page']) )
            driver.add_page(cm)
        def getpage(cm):
            print("Page: %s" % (cm['page']) )
            driver.get_page(cm)
        def addelement(cm):
            print("Page: %s Object: %s Value: %s" % (cm['page'],cm['object'],cm['value']) )
            driver.add_element(cm)
        def getelement(cm):
            print("Page: %s" % cm['object'])
        def scroll(cm):
            print("Scroll: %s" % cm['object'])
        def submit(cm):
            print("Submit: %s" % cm['object'])
            driver.do_submit(cm)
        def inject(cm):
            driver.inject_text(cm)
        def click(cm):
            print("Click: %s" % cm['object'])
            driver.wait_until_clickable(cm)
        def wait(cm):
            print("Wait: %s" % cm['object'])
            driver.wait_until_element_located(cm)
        self.func_list = vars()
    def execute(self,cm):
        self.func_list[cm['event']](cm)
    def __del__(self):
        self.func_list = None
