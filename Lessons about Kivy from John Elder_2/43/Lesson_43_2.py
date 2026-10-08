from kivy.lang import Builder
from kivy.properties import ColorProperty
from kivymd.app import MDApp
from kivy.utils import get_color_from_hex


class MainApp(MDApp):

    # Поточні кольори
    button_1_color = ColorProperty(
        get_color_from_hex("#FF1493")
    )

    button_2_color = ColorProperty(
        get_color_from_hex("#00CED1")
    )

    button_3_color = ColorProperty(
        get_color_from_hex("#8A2BE2")
    )

    text_color = ColorProperty(
        get_color_from_hex("#000000")
    )

    current_theme = "colorful"

    def change_theme(self):
        if self.current_theme == "colorful":

            self.button_1_color = get_color_from_hex("#2196F3")
            self.button_2_color = get_color_from_hex("#4CAF50")
            self.button_3_color = get_color_from_hex("#F44336")
            self.text_color = get_color_from_hex("#FFFFFF")

            self.current_theme = "standard"

        else:

            self.button_1_color = get_color_from_hex("#FF1493")
            self.button_2_color = get_color_from_hex("#00CED1")
            self.button_3_color = get_color_from_hex("#8A2BE2")
            self.text_color = get_color_from_hex("#000000")

            self.current_theme = "colorful"

    def light_theme(self):

            self.button_1_color = get_color_from_hex("#2196F3")
            self.button_2_color = get_color_from_hex("#4CAF50")
            self.button_3_color = get_color_from_hex("#F44336")
            self.text_color = get_color_from_hex("#FFFFFF")

            self.current_theme = "standard"


    def dark_theme(self):

            self.button_1_color = get_color_from_hex("#FF1493")
            self.button_2_color = get_color_from_hex("#00CED1")
            self.button_3_color = get_color_from_hex("#8A2BE2")
            self.text_color = get_color_from_hex("#000000")

            self.current_theme = "colorful"

    def build(self):
        return Builder.load_file("Color_theme_43_2.kv")


MainApp().run()