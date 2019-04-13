
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

class Action():
    def __init__(self,c):
        self.events = []
    def add_action(self,c):
        pass
    def get_action(self):
        return self.events
