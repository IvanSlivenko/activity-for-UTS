import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.spelling import Spelling


#Set the app size
Window.size = (700,500)

Builder.load_file('CheckBoxes_29.kv')

class MyLayout(Widget):
    checs = []
    def checkbox_click(self, instance, value, topping):
        if value == True:
            MyLayout.checs.append(topping)
            tops = ''
            for x in MyLayout.checs:
                tops = f'{tops} {x}'
            self.ids.output_label.text=f' You selected: {tops}'
        else:
            MyLayout.checs.remove(topping)
            tops = ''
            for x in MyLayout.checs:
                tops = f'{tops} {x}'
            self.ids.output_label.text = f' You selected: {tops}'

class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
