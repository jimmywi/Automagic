#!/Users/jimmy/miniconda3/envs/selenv/bin/python
#coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class driverChrome(metaclass=Singleton):
    def __init__(self):
        self.driver = None 
    def getInstance(self):
        if self.driver == None:
            chrome_path = '/Users/jimmy/Developer/Automagic/chromedriver'
            self.driver = webdriver.Chrome(chrome_path)
        return self.driver
    def waitUntilClickable(self, elementID):
        wait = WebDriverWait(self.driver,10)
        element = wait.until(EC.element_to_be_clickable((By.ID, elementID)))
    def waitUntilElementLocated(self, elementID):
        wait = WebDriverWait(self.driver,10)
        element = wait.until(EC.presence_of_element_located((By.NAME, elementID)))

class XCommand():
    def __init__(self):
        def open(cm):
            print("Open: %s" % cm['input'])
        def path(cm):
            print("Path: %s" % cm['input'])
        def textbox(cm):
            print("Textbox: %s" % cm['input'])
        def getelems(cm):
            print("Elements: %s" % cm['input'])
        def getelem(cm):
            print("Ekement: %s" % cm['input'])
        def scroll(cm):
            print("Sroll: %s" % cm['input'])
        def submit(cm):
            print("Submit: %s" % cm['input'])
        def click(cm):
            print("Click: %s" % cm['input'])
        self.func_list = vars()
    def execute(self,cm):
        self.func_list[cm['type']](cm)
    def __del__(self):
        self.func_list = None

class app:
    def __init__(self):
        pass
    def run(self):
        xc = XCommand()
        xc.execute({'type':'open', 'input':'https://google.com'})
        driver = driverChrome().getInstance()
        print(hex(id(driver)))
        driver.get('http://www.google.com/xhtml')
        driverChrome().waitUntilElementLocated('q')
        search_box = driver.find_element_by_name('q')
        search_box.send_keys('Apple Pie')
        search_box.submit()
        driverChrome().waitUntilElementLocated('q')

if __name__ == "__main__":
    web = driverChrome().getInstance()
    print(hex(id(web)))
    ap = app()
    ap.run()
    time.sleep(5)
    web.close()
    web.quit()
