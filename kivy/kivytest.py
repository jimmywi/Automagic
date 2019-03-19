import kivy
kivy.require('1.10.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CustomGrid(GridLayout):
    pass

class HelloApp(App):
    kv_directory = 'kv'
    def build(self):
        return CustomGrid()

if __name__ == '__main__':
    HelloApp().run()
