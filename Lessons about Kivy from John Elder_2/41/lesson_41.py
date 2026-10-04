import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp


#Set the app size
Window.size = (700,500)

Builder.load_file('Card_41.kv')



class MyLayout(Widget):
    pass


class AwesomeApp(MDApp):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        return MyLayout()


if __name__ == "__main__":
    AwesomeApp().run()
