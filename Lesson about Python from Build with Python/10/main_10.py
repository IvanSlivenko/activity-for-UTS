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



class Lesson_10_App(MDApp):

    def build(self):
        #---------------------------------------------------- Togle Theme
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"
        #---------------------------------------------------- Togle Theme

        screen = Screen()
        table = MDDataTable(
            pos_hint={'center_x': 0.5,'center_y': 0.5},
            size_hint=(0.9, 0.6),
            check=True,    
            rows_num=10, 
            column_data=[
                ("No", dp(18)),
                ("Food", dp(20)),
                ("Calories", dp(20))
            ],
            row_data = [
                ("1", "Burger","300"),
                ("2", "Toast","150"),
                ("3", "Toast","150"),
                ("4", "Toast","150"),
                ("5", "Toast","150"),
                ("6", "Toast","150"),
                ("7", "Toast","150"),
                ("8", "Toast","150"),
                ("9", "Toast","150"),
                
            ]
        )
        

        table.bind(on_check_press=self.chek_press)
        table.bind(on_row_press=self.row_press)
        screen.add_widget(table)
        
        return screen   

    def chek_press(self, instance_table, current_row):
        print(instance_table, current_row)

    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)    



Lesson_10_App().run()


