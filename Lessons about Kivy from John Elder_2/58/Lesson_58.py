
from kivy.config import Config
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', 1110)
Config.set('graphics', 'top', 400)

from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.metrics import sp
from kivy.core.window import Window




class ClickableBox(ButtonBehavior, MDBoxLayout):
    pass


class MainApp(MDApp):

    def on_start(self):
        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

    def build(self):
        Window.borderless = True
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

 

        return Builder.load_file("Lesson_58.kv")






MainApp().run()
