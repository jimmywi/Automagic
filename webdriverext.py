from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from event_handler import Page
from event_handler import Action

class WebDriverChromeExt(webdriver.Chrome):
    def __init__( self, path ):
        webdriver.Chrome.__init__( self, path )
        self.pages = {}
        self.actions = [] 
    def add_events(self,cm):
        self.actions.append(cm)
    def get_events(self):
        return self.actions
    def add_page(self, cm):
        self.pages[cm['page']] = Page(cm)
    def get_page(self, cm):
        return self.pages[cm['page']].get_url()
    def add_element(self, cm):
        self.pages[cm['page']].add_element(cm)
        print('add element')
        for k, v in self.pages.items():
           #print(k, v)
            for ki, kv in v.get_elements().items():
                print(ki, kv)
    def get_element(self, cm):
        return self.pages[cm['page']].get_element(cm)
    def clear_pages(self):
        del self.pages
    def do_submit(self,cm):
        xpath = self.pages[cm['page']].get_element(cm)
        self.wait_until_element_located(cm)
        element = self.find_element(By.XPATH, xpath)
        element.submit()
    def inject_text(self, cm):
        js_syntax = """
                    (document.evaluate('%s',document,null,
                    XPathResult.FIRST_ORDERED_NODE_TYPE,
                    null).singleNodeValue).value='%s';
                    """ 
        self.wait_until_element_located(cm)
        xpath = self.pages[cm['page']].get_element(cm)
        js_syntax = js_syntax % (xpath, cm['value'])
        self.execute_script(js_syntax)
    def wait_until_clickable(self, cm):
        print("Wait until clickable") 
        wait = WebDriverWait(self,10)
        xpath = self.pages[cm['page']].get_element(cm)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    def wait_until_element_located(self, cm):
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
