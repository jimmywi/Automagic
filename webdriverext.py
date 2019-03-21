
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class WebDriverChromeExt(webdriver.Chrome):
    def __init__( self, path ):
        webdriver.Chrome.__init__( self, path )
        self.elementList = {}

    def setElementList(self, cm):
        self.elementList[cm['object']] = cm['value']
        for k, v in self.elementList.items():
            print(k, v)

    def getElementList(self, cm):
        return self.elementList[cm['object']]
 
    def clearElementList(self):
        del self.elementList

    def injectText(self, cm):
        js_syntax = "(document.evaluate('" + self.elementList[cm['object']] + "', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue).value='"+ cm['value']  +"';"
        self.execute_script(js_syntax)

    def waitUntilClickable(self, cm):
        print("Wait until clickable") 
        wait = WebDriverWait(self,10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, cm['object'])))

    def waitUntilElementLocated(self, cm):
        print("Wait until element located") 
        wait = WebDriverWait(self,10)
        element = wait.until(EC.presence_of_element_located((By.XPATH, self.elementList[cm['object']])))

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
