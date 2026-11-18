from kivymd.uix.bottomnavigation.bottomnavigation import WindowSDL
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
# from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.toolbar import MDTopAppBar

#--------------------------------------------------------------------
from kivy.uix.floatlayout import FloatLayout
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
from kivy.core.window import Window

from kivy.metrics import dp
from kivy.clock import Clock


Window.size = (300, 500)

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Lesson_11'
            left_action_items: [["menu", lambda x: app.navigation_draw() ]]
            right_action_items: [["clock", lambda x: app.clock_draw() ]]
            elevation: 8
        MDLabel:
            text: 'Label Lesson_11'
            halign: 'center'
        
        MDBottomAppBar:
            MDTopAppBar:
                # title: 'Help'
                icon: 'plus'
                type: 'bottom'
                # mode: 'center'
                mode: 'end'
                # mode: 'free-end'  
                left_action_items: [["coffee", lambda x: app.navigation_draw() ]]
                on_action_button: app.central_button_action()
        
                  


"""

class Lesson_11_App(MDApp):

    def build(self):
        #---------------------------------------------------- Togle Theme
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"
        #---------------------------------------------------- Togle Theme

        screen = Builder.load_string(screen_helper) 

        
        return screen   


    
    # def on_start(self):
    #     Clock.schedule_once(self.move_bottom_button, 0.5)

    # region move_bottom_button 
    # def move_bottom_button(self, *args):

    #     bottom_bar = self.root.children[0].children[0]

    #     for widget in bottom_bar.walk():
    #         print(widget.__class__.__name__, widget.pos)

    #         if widget.__class__.__name__ == "ActionBottomAppBarButton":

    #             print("Знайдено FAB:", widget)
    #             print("Початкова позиція:", widget.pos)

    #             widget.y += dp(120)

    #             print("Нова позиція:", widget.pos)
    #             break
    #endregion




    def navigation_draw(self):
        print("navigation")

    def clock_draw(self):
        print("clock")

    def central_button_action(self):

        self.dialog = MDDialog(
            title="Центральна кнопка",
            text="Ти натиснув FAB!",
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: self.dialog.dismiss()
                )
            ]
        )

        self.dialog.open()


Lesson_11_App().run()


