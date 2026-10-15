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
    
    def presser_left_button(self):
        self.root.ids.my_label.text = "You pressed left_button!!"

    def presser_midle_button(self):
        self.root.ids.my_label.text = "You pressed midle_button!!"

    def presser_right_button(self):
        self.root.ids.my_label.text = "You pressed right_button!!"
    
        

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

        return Builder.load_file("botomButton_46.kv") 


MainApp().run()