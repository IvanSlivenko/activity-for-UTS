
from kivy.lang import Builder
from kivy.properties import ColorProperty
from kivy.animation import Animation
from kivy.utils import get_color_from_hex
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText
from kivy.clock import Clock
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogHeadlineText,
    MDDialogContentContainer,
    MDDialogButtonContainer,
)
from kivymd.uix.label import MDLabel
from kivy.metrics import sp
# from kivymd.uix.picker import MDDatePicker
from kivymd.uix.pickers import MDModalDatePicker
# from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.pickers import MDTimePickerDialVertical
from kivymd.uix.pickers import MDTimePickerInput
from datetime import datetime
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp



class ClickableBox(ButtonBehavior, MDBoxLayout):
    pass

class MainApp(MDApp):



    def on_start(self):
            self.theme_cls.theme_style = "Dark"
            # self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Blue"
#-----------------------------------------    


#-----------------------------------------
    def build(self):
        
        screen = Screen()

        table = MDDataTable(
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            size_hint = (0.9, 0.6),
            column_data= [
                ("First Name", dp(30)),
                ("Last Name", dp(30)),
                ("Email Adress", dp(50)),
                ("Phone Number", dp(30))
            ],
            row_data = [
                ("Jhon","Elder","UmanProger@urk.net","067 470 87 19" ),
                ("Forest","Gamp","UmanProger@urk.net","067 470 87 20" ),
                ("Ivan","Slivenko","UmanProger@urk.net","067 470 87 21" ),
                
            ]

        )




        self.theme_cls.font_styles["Welcome"] = {
            "large": {
                "line-height": 1.2,
                "font-name": "Roboto",
                "font-size": sp(40),
            },
            "medium": {
                "line-height": 1.2,
                "font-name": "Roboto",
                "font-size": sp(36),
            },
            "small": {
                "line-height": 1.2,
                "font-name": "Roboto",
                "font-size": sp(24),
            },
        }



        # root = Builder.load_file("table_53.kv")
        
        # return root

        screen.add_widget(table)
        return screen

    

MainApp().run()