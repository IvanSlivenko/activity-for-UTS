

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.utils import get_color_from_hex



class Lesson_2_App(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        label = MDLabel(
            text="Hello from Kivy Label",
            halign="center",
            valign="middle",
            theme_text_color='Custom',
            text_color=get_color_from_hex("#00FF00")
            )
        return label    



Lesson_2_App().run()
