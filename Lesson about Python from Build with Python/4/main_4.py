from kivymd.uix.button import MDFloatingActionButton

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen



from kivy.utils import get_color_from_hex


class Lesson_4_App(MDApp):

    def build(self):
        # -------------------------------------------- block Thene Togle
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.primary_hue = "500"
        # -------------------------------------------- block Thene Togle
        screen = Screen()

        btn_flat = MDFlatButton(
            text="Flat Button",
            pos_hint={'center_x':0.5, 'center_y':0.5}
        )


        btn_rectangle = MDRectangleFlatButton(
            text="Flat Button",
            pos_hint={'center_x':0.5, 'center_y':0.4}
        )

        icon_dtn = MDIconButton(
            icon='language-python',
            pos_hint= {"center_x": 0.5, "center_y": 0.3}
        )

        action_btn = MDFloatingActionButton(
            icon='language-python',
            pos_hint= {"center_x": 0.5, "center_y": 0.2}
        )

        screen.add_widget(btn_flat) 
        screen.add_widget(btn_rectangle)    
        screen.add_widget(icon_dtn)
        screen.add_widget(action_btn)

        return screen   



Lesson_4_App().run()


