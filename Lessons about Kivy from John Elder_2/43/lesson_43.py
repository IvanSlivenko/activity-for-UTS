
from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        # self.theme_cls.primary_palette="Gray"
        # self.theme_cls.accent_palette = "White"
        return Builder.load_file('Color_theme_43.kv')


MainApp().run()

