

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class Lesson_1_App(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        return MDLabel(
            text="Hello from KivyMD!",
            halign="center",
            valign="middle"
        )


Lesson_1_App().run()
