from kivymd.uix.banner.banner import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import (MDFlatButton, MDRectangleFlatButton, 
    MDIconButton, MDFloatingActionButton, MDFlatButton)
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog

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
            pos_hint= {'center_x': 0.5, 'center_y': 0.4},
            on_release=self.show_data
            
            )
        
        self.username =Builder.load_string(user_name_helper)

        screen.add_widget(self.username)
        screen.add_widget(button)    
        

        return screen   

    def  show_data(self, obj):
        if self.username.text is "":
            check_string = "Pleese enter a username"
        else:
            check_string = self.username.text + ' does not exist'

        close_button = MDFlatButton(
            text="Close",
            on_release=self.close_diflog
            )

        more_button = MDFlatButton(
            text="More..."
            )

        self.dialog = MDDialog(
            title='Username Check',
            text=check_string,
            size_hint = (0.7, 1),
            buttons=[close_button, more_button]
        )
        self.username.text=""
        self.dialog.open()

    def close_diflog(self, obj):
        self.dialog.dismiss()




Lesson_5_App().run()


