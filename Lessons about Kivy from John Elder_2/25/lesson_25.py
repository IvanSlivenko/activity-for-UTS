import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.spelling import Spelling



#print("Spelling",Spelling)

#from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.image import Image

#Set the app size
Window.size = (700,500)

Builder.load_file('slider_25.kv')

class MyLayout(Widget):
    def slide_it(self, *args):
        self.ids.slider_label.text=str(args[1])
        self.ids.slider_label.font_size = self.ids.slider_label.font_size+args[1]
        # print(args[1])
class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
