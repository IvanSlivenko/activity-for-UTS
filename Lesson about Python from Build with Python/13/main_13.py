
#region Imports
from kivy.uix.bubble import Image
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.uix.filechooser import ScreenManager
from kivymd.uix.bottomnavigation.bottomnavigation import WindowSDL
from kivymd.uix.datatables import MDDataTable
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
#endregion

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
            BoxLayout:
                orientation: "vertical"
                spacing: '8dp'
                padding: '8dp'


                Image:
                    source: '1.jfif'
                    size_hint_y: None
                    height: "300dp"
                    allow_stretch: True
                    keep_ratio: True


                MDLabel:
                    text: "UmanProger"
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "UmanProger@ukr.net"
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: "Profile"
                            IconLeftWidget:
                                icon: 'account'

                        OneLineIconListItem:
                            text: "Email"
                            IconLeftWidget:
                                icon: 'email-outline'

                        OneLineIconListItem:
                            text: "Upload"
                            IconLeftWidget:
                                icon: 'cloud-upload-outline'

                        OneLineIconListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon: 'logout'         

"""

class Lesson_13_App(MDApp):

    def build(self):
        #region Togle_Theme

        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "500"

        #endregion

        screen = Builder.load_string(navigation_helper)  

        
        return screen   

Lesson_13_App().run()


