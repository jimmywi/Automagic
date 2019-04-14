from webdriverext import ChromeDriverExt

class WebCommand():
    def __init__(self):
        driver = ChromeDriverExt().getInstance()
        def open(c):
            print("Open: %s" % c['page'])
            driver.open_url(c)
        def scroll(c):
            print("Scroll: %s" % c['object'])
        def submit(c):
            print("Submit: %s" % c['object'])
            driver.do_submit(c)
        def inject(c):
            driver.inject_text(c)
        def click(c):
            print("Click: %s" % c['object'])
            driver.wait_until_clickable(c)
        def wait(c):
            print("Wait: %s" % c['object'])
            driver.wait_until_element_located(c)
        self.func_list = vars()
    def execute(self,c):
        self.func_list[c['event']](c)
    def __del__(self):
        self.func_list = None
