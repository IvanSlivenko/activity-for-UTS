import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import  ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel

#Set the app size
Window.size = (700,500)

Builder.load_file('button_image_35.kv')

class MyLayout(Widget):
    pass


class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
