from kivymd.uix.banner.banner import OneLineListItem

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

        
        # --------------------------------------------------------- list_view
        list_view = MDList()

        for i in range(20):
            # items = OneLineListItem(text='Item '+ str(i+1))
            # items = TwoLineListItem(text='Item '+ str(i+1), secondary_text= 'Description '+ str(i+1))
            items = ThreeLineIconListItem(
                text='First Name '+ str(i+1), 
                secondary_text= 'Last Name '+ str(i+1),
                tertiary_text= 'Age '+ str(i+1)
                )
            list_view.add_widget(items)


        
        
        # ---------------------------------------------------- ScrollView
        scroll = ScrollView()
        scroll.add_widget(list_view) 


        #----------------------------------------------------- Screen
        screen = Screen()
        screen.add_widget(scroll)    


        return screen   





Lesson_8_App().run()


