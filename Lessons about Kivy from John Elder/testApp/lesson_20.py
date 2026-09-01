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

#Builder.load_file('calc.kv')

#---------------------------------
import os
import sys

if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

Builder.load_file(os.path.join(BASE_DIR, "calc.kv"))
#---------------------------------


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text=str(0)

    def remove(self):
        prior = self.ids.calc_input.text
        prior=prior[:-1]
        self.ids.calc_input.text=prior

    #Create a button pressing function
    def button_press(self, button):
        prior=self.ids.calc_input.text

        # test fo error first
        if "Error" in prior:
            prior = ''

        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}{sign}'

    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")


        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

        elif "." in prior:
            pass
        else:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior

    def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-","")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    def eguals(self):
            prior = self.ids.calc_input.text
            #error handling
            try:
                answer = eval(prior)
                self.ids.calc_input.text = str(answer)
            except:
                self.ids.calc_input.text="Error"


            # if "+" in prior:
            #     num_list=prior.split("+")
            #     #print('num_list',num_list)
            #     answer = 0.0
            #     for number in num_list:
            #         answer = answer + float(number)
            #     self.ids.calc_input.text = str(answer)
            # if "+" in prior:
            #     num_list=prior.split("+")
            #     #print('num_list',num_list)
            #     answer = 0
            #     for number in num_list:
            #         answer = answer + float(number)
            #     self.ids.calc_input.text = str(answer)
            #


class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    CalculatorApp().run()
