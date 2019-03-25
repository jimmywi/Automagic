from webdriverext import ChromeDriverExt

class WebCommand():
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
