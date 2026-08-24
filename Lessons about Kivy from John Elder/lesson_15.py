import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

#from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.image import Image

#Set the app size
Window.size = (500,700)

Builder.load_file('kivygui/calc.kv')



class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text=0

    #Create a button pressing function
    def button_press(self, button):
        #pass
        prior=self.ids.calc_input.text

        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text += str(button)



class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    CalculatorApp().run()
