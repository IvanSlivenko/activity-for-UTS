from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.uix.filechooser import ScreenManager
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
from kivymd.uix.navigationdrawer import MDNavigationLayout


Window.size = (300, 500)



navigation_helper = """ 
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:

                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Lesson_11'
                        # left_action_items: [["menu", lambda x: app.nav_drawer.toggle_nav_drawer() ]]
                        # left_action_items: [["menu", lambda x: root.ids.nav_drawer.toggle_nav_drawer()]]
                        left_action_items: [["menu", lambda x: root.ids.nav_drawer.set_state("toggle")]]
                        elevation: 7

                    Widget:




        MDNavigationDrawer:
            id: nav_drawer                    

"""

class Lesson_12_App(MDApp):

    def build(self):
        #region Togle_Theme

        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "500"

        #endregion
        # screen = Builder.load_string(screen_helper)
        screen = Builder.load_string(navigation_helper)  

        
        return screen   





Lesson_12_App().run()


