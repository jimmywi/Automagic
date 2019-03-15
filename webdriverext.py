
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class WebDriverChromeExt(webdriver.Chrome):

    def setElementList(self, elementID, tagID):
        pass

    def getElementList(self, tagID):
        pass

    def waitUntilClickable(self, elementID):
        print("Wait until clickable") 
        wait = WebDriverWait(self,10)
        element = wait.until(EC.element_to_be_clickable((By.ID, elementID)))

    def waitUntilElementLocated(self, elementID):
        print("Wait until element located") 
        wait = WebDriverWait(self,10)
        element = wait.until(EC.presence_of_element_located((By.NAME, elementID)))

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ChromeDriverExt(metaclass=Singleton):
    def __init__(self):
        self.driver = None 
        self.elementList = []
    def getInstance(self):
        if self.driver == None:
            chrome_path = '/Users/jimmy/Developer/Automagic/chromedriver'
            self.driver = WebDriverChromeExt(chrome_path)
        return self.driver

