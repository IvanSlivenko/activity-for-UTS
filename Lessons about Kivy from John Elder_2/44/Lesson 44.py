from kivy.lang import Builder
from kivy.properties import ColorProperty
from kivymd.app import MDApp
from kivy.utils import get_color_from_hex

from kivy.metrics import sp


class MainApp(MDApp):

    def on_start(self):
            self.theme_cls.theme_style = "Dark"
            # self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Blue"

    def logger(self):
        self.root.ids.welcome_label.text = f'Sup {self.root.ids.user.text}!'
          

    def clear(self):
        self.root.ids.welcome_label.text = 'Welcome'
        self.root.ids.user.text = '' 
        self.root.ids.pasword.text = ''    



    def build(self):

        #------------------------------------------------ font_style
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
        #------------------------------------------------ font_style       

        return Builder.load_file("login_44.kv") 


MainApp().run()