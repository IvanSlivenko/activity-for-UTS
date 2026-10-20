

from kivy.lang import Builder
from kivy.properties import ColorProperty
from kivy.animation import Animation
from kivy.metrics import dp
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

class ClickableBox(ButtonBehavior, MDBoxLayout):
    pass

class MainApp(MDApp):



    def on_start(self):
            self.theme_cls.theme_style = "Dark"
            # self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Blue"
    
   


    def build(self):
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

        root = Builder.load_file("swiper_50.kv")
        
        return root

    

MainApp().run()