from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivy.utils import get_color_from_hex


class Lesson_2_App(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

        
        label = MDLabel(
            text="Hello from Kivy Label",
            halign="center",
            # valign="middle",
            pos_hint= {"center_x": 0.5, "center_y": 0.5},
            theme_text_color='Custom',
            text_color=get_color_from_hex("#00FF00"),
            font_style="Caption"
            )

        icon_label = MDIcon(
            icon='language-python',
            pos_hint= {"center_x": 0.5, "center_y": 0.4}
            ) 

        layout = FloatLayout(

        )

        layout.add_widget(label)
        layout.add_widget(icon_label)

        return layout   



Lesson_2_App().run()


