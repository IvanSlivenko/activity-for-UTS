from kivy.lang import Builder
from kivy.properties import ColorProperty
from kivymd.app import MDApp
from kivy.utils import get_color_from_hex


class MainApp(MDApp):

    def on_start(self):
            self.theme_cls.theme_style = "Dark"
            # self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Blue"




    def build(self):
        return Builder.load_file("login_44.kv")


MainApp().run()