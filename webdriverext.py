from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from page import Page

class WebDriverChromeExt(webdriver.Chrome):
    def __init__( self, path ):
        webdriver.Chrome.__init__( self, path )
        self.pages = {}
    def addPage(self, cm):
        self.pages[cm['page']] = Page(cm)
    def getPage(self, cm):
        return self.pages[cm['page']].get_url()
    def addElement(self, cm):
        self.pages[cm['page']].add_element(cm)
        print('add element')
        for k, v in self.pages.items():
           #print(k, v)
            for ki, kv in v.get_elements().items():
                print(ki, kv)
    def getElement(self, cm):
        return self.pages[cm['page']].get_element(cm)
 
    def clearElementList(self):
        del self.pages

    def injectText(self, cm):
        js_syntax = """
        (document.evaluate('%s',
        document,
        null,
        XPathResult.FIRST_ORDERED_NODE_TYPE,
        null).singleNodeValue)
        .value='%s';
        """ 
        xpath = self.pages[cm['page']].get_element(cm)
        js_syntax = js_syntax % (xpath, cm['value'])
        self.execute_script(js_syntax)

    def waitUntilClickable(self, cm):
        print("Wait until clickable") 
        wait = WebDriverWait(self,10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, pages[cm['page']][cm['object']])))

    def waitUntilElementLocated(self, cm):
        print("Wait until element located") 
        wait = WebDriverWait(self,10)
        xpath = self.pages[cm['page']].get_element(cm)
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ChromeDriverExt(metaclass=Singleton):
    def __init__(self):
        self.driver = None 
    def getInstance(self):
        if self.driver == None:
            chrome_path = './chromedriver'
            self.driver = WebDriverChromeExt(chrome_path)
        return self.driver
