from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class WebDriverChromeExt(webdriver.Chrome):
    def __init__( self, path ):
        webdriver.Chrome.__init__( self, path )
        self.pages = {}
    def set_pages(self, pages):
        self.pages = pages
    def open_url(self,c):
        print(c['page'])
        print(self.pages[c['page']].get_url())
        self.get(self.pages[c['page']].get_url())
    def do_submit(self,c):
        print(c)
        xpath = self.pages[c['page']].get_element(c)
        self.wait_until_element_located(c)
        element = self.find_element(By.XPATH, xpath)
        element.submit()
    def inject_text(self, c):
        js_syntax = """
                    (document.evaluate('%s',document,null,
                    XPathResult.FIRST_ORDERED_NODE_TYPE,
                    null).singleNodeValue).value='%s';
                    """ 
        self.wait_until_element_located(c)
        xpath = self.pages[c['page']].get_element(c)
        js_syntax = js_syntax % (xpath, c['value'])
        self.execute_script(js_syntax)
    def wait_until_clickable(self, c):
        print("Wait until clickable") 
        wait = WebDriverWait(self,10)
        xpath = self.pages[c['page']].get_element(c)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    def wait_until_element_located(self, c):
        print("Wait until element located") 
        wait = WebDriverWait(self,10)
        xpath = self.pages[c['page']].get_element(c)
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
