from kivy.uix.gridlayout import GridLayout
from kivy.uix.actionbar import Label
from kivy.metrics import sp
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.vkeyboard import VKeyboard
from kivy.uix.label import Label
from kivy.uix.gridLayout import gridLayout



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
        # return Builder.load_file('Lesson_62.kv')

        # Define Our Laoyout
        layout = GridLayout(cols=1)

        #Define Our VKeyboard
        keyboard = VKeyboard(on_key_up=self.key_up)

        layout.add_widget(self.label)
        layout.add_widget(keyboard)

        return layout

    def key_up(self):
        pass






MainApp().run()       

