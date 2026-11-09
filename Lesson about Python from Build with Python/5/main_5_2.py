from kivymd.uix.pickers.datepicker.datepicker import MDTextField
from kivymd.uix.button import MDFloatingActionButton

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.textfield import MDTextField

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen

from kivy.utils import get_color_from_hex
from kivy.lang import Builder

user_name_helper = """ 
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    # helper_text_mode: "persistent"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width: 300
"""

class Lesson_5_App(MDApp):

    def build(self):
        # -------------------------------------------- block Thene Togle
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"
        # -------------------------------------------- block Thene Togle
        screen = Screen()

        # username = MDTextField(
        #     text= 'Enter username',
        #     pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #     # size_hint=(0.5, 1)
        #     size_hint_x = None,
        #     width=300

        # )
        
        username =Builder.load_string(user_name_helper)

        screen.add_widget(username)    
        

        return screen   



Lesson_5_App().run()


