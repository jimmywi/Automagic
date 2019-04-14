
class EventHandler():
    def __init__(self):
        self.pages = {}
        self.actions = []
    def add_page(self,c):
        self.pages[c['page']] = Page(c)
        print(self.pages[c['page']])
    def get_page(self,c):
        return self.pages[c['page']].get_url()
    def get_pages(self):
        return self.pages
    def add_page_element(self,c):
        self.pages[c['page']].add_element(c)
    def get_page_element(self,c):
        return self.pages[c['page']].get_element(c)
    def add_action(self,c):
        self.actions.append(c)
    def get_actions(self):
        return self.actions

class Page():
    def __init__(self,c):
        self.url = c['url']
        self.elements = {}
    def add_element(self,c):
        self.elements[c['object']] = c['value']
    def get_element(self,c):
        return self.elements[c['object']]
    def get_elements(self):
        return self.elements
    def get_url(self):
        return self.url

