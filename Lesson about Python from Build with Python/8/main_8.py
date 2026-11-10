
#--------------------------------------------------------------------
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import (MDFlatButton, MDRectangleFlatButton, 
    MDIconButton, MDFloatingActionButton, MDFlatButton)
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.uix.floatlayout import FloatLayout
from kivy.utils import get_color_from_hex
from kivy.lang import Builder
#--------------------------------------------------------------------
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView

from kivymd.app import MDApp
from kivymd.uix.list import (
    OneLineListItem,
    TwoLineListItem,
    ThreeLineListItem,
    OneLineIconListItem,
    TwoLineIconListItem,
    ThreeLineIconListItem,
    MDList
)



class Lesson_8_App(MDApp):

    def build(self):
        # -------------------------------------------- block Thene Togle
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"
        # -------------------------------------------- block Thene Togle

        screen = Screen()

        self.item_1 = OneLineListItem(
            text = 'Item 1'
        )
        

        screen.add_widget(self.item_1)    
        

        return screen   

#---------------------------------------------------------
        # scroll = ScrollView()
        # list_view = MDList()

        # list_view.add_widget(
        #     OneLineListItem(text="First item")
        # )

        # list_view.add_widget(
        #     OneLineListItem(text="Second item")
        # )

        # scroll.add_widget(list_view)

        # return scroll
#----------------------------------------------------------



Lesson_8_App().run()


