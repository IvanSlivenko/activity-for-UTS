import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import  ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanel

#Set the app size
Window.size = (700,500)

Builder.load_file('button_image_36.kv')

class MyLayout(Widget):
    def hello_on(self):

        self.ids.my_image.source = "../images/jungle-canopy-image.webp"
    def hello_off(self):
        self.ids.my_image.source = "../images/jungle.jpg"
        self.ids.my_label.text = "You Pressed The Button"



class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
