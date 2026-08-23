import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.image import Image

Builder.load_file('kivygui/update_label.kv')



class MyLayout(Widget):
    def press(self):
        #Create variables for our widgets
        name = self.ids.name_input.text
        #print("name : ",name)

        #Update the Label
        self.ids.name_label.text=f'Ви написали : {name}'

        #Clear input box
        self.ids.name_input.text = ''

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
