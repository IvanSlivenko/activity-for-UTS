import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.spelling import Spelling
from kivy.uix.screenmanager import ScreenManager, Screen

class MyLayout(Widget):
    pass



#Set the app size
Window.size = (700,500)

Builder.load_file('split_33.kv')


class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
