

from kivy.lang import Builder
from kivy.properties import ColorProperty
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.utils import get_color_from_hex

from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText

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

    dialog = None

    def on_start(self):
            self.theme_cls.theme_style = "Dark"
            # self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Blue"
    
    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                MDDialogHeadlineText(
                    text="Pretty Neat, Right?"
                ),
                MDDialogContentContainer(
                    MDLabel(
                        text="Your message goes here",
                        adaptive_height=True,
                    ),
                    orientation="vertical",
                    padding=dp(24),
                ),
                MDDialogButtonContainer(
                    MDButton(
                        MDButtonText(text="CANCEL"),
                        style="text",
                        on_release=lambda *args: self.dialog.dismiss(),
                    ),
                    spacing=dp(8),
                    padding=dp(8),
                ),
            )

        self.dialog.open()


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

        root = Builder.load_file("alert_48.kv")
       

        return root

    

MainApp().run()