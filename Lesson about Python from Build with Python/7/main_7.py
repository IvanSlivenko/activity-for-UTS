from kivymd.uix.behaviors.toggle_behavior import MDRectangleFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.textfield import MDTextField

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen

from kivy.utils import get_color_from_hex
from kivy.lang import Builder

from helpers import user_name_helper

class Lesson_5_App(MDApp):

    def build(self):
        # -------------------------------------------- block Thene Togle
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"
        # -------------------------------------------- block Thene Togle

        screen = Screen()

        button = MDRectangleFlatButton(
            text="Show",
            pos_hint= {'center_x': 0.65, 'center_y': 0.4},
            on_release=self.show_data
            
            )
        
        self.username =Builder.load_string(user_name_helper)

        screen.add_widget(self.username)
        screen.add_widget(button)    
        

        return screen   

    def  show_data(self, obj):
        print(self.username.text)
        self.username.text=""

Lesson_5_App().run()


