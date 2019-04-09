from webdriverext import ChromeDriverExt

class WebCommand():
    def __init__(self):
        driver = ChromeDriverExt().getInstance()
        def open(cm):
            print("Open: %s" % cm['page'])
            driver.get(driver.getPage(cm))
        def addpage(cm):
            print("Page: %s" % (cm['page']) )
            driver.addPage(cm)
        def getpage(cm):
            print("Page: %s" % (cm['page']) )
        def addelement(cm):
            print("Page: %s Object: %s Value: %s" % (cm['page'],cm['object'],cm['value']) )
            driver.addElement(cm)
        def getelement(cm):
            print("Page: %s" % cm['object'])
        def scroll(cm):
            print("Scroll: %s" % cm['object'])
        def submit(cm):
            print("Submit: %s" % cm['object'])
            xpath = driver.getElement(cm)
            el = driver.find_element_by_xpath(xpath)
            el.submit()
        def inject(cm):
            driver.injectText(cm)
        def click(cm):
            print("Click: %s" % cm['object'])
            driver.waitUntilClickable(cm)
        def wait(cm):
            print("Wait: %s" % cm['object'])
            driver.waitUntilElementLocated(cm)
        self.func_list = vars()
    def execute(self,cm):
        self.func_list[cm['event']](cm)
    def __del__(self):
        self.func_list = None
