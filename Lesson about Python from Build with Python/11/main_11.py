from kivymd.uix.datatables import MDDataTable
from kivymd.uix.list import MDList
from kivymd.uix.list import ImageRightWidget
from kivymd.uix.list import ThreeLineIconListItem
from kivymd.uix.banner.banner import OneLineListItem
from kivy.utils import get_color_from_hex


#--------------------------------------------------------------------
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.button import (MDFlatButton, MDRectangleFlatButton, 
    MDIconButton, MDFloatingActionButton, MDFlatButton)
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.uix.floatlayout import FloatLayout


#--------------------------------------------------------------------
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.list import (
    OneLineListItem,
    TwoLineListItem,
    ThreeLineListItem,
    OneLineIconListItem,
    TwoLineIconListItem,
    ThreeLineIconListItem,
    ThreeLineAvatarIconListItem,
    MDList,
    IconLeftWidget,
    IconRightWidget,
    ImageRightWidget
)
from kivymd.uix.datatables import MDDataTable

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Lesson_11'

"""

class Lesson_11_App(MDApp):

    def build(self):
        #---------------------------------------------------- Togle Theme
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"
        #---------------------------------------------------- Togle Theme

        screen = 

        
        return screen   

   



Lesson_11_App().run()


