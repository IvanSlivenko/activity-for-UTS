from kivymd.uix.behaviors.toggle_behavior import MDRectangleFlatButton

#region Imports
from kivy.uix.bubble import Image
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.uix.screenmanager import Screen, ScreenManager
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

Window.size = (300, 700)

screen_helper = """ 
ScreenManager:
    MenuScreen:
    ProfileScreen:
    ProductsScreen:
    ContactsScreen:


<MenuScreen>:
    name: 'menu'
    MDLabel:  
        text: 'Screen Menu'
        halign: 'center'

    MDRectangleFlatButton:  
        text: 'Profile'
        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
        on_press: root.manager.current = 'profile'

<ProfileScreen>:
    name: 'profile'
    MDLabel:  
        text: 'Screen Profile'
        halign: 'center'

    MDRectangleFlatButton:  
        text: 'Products'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'products' 

<ProductsScreen>:
    name: 'products'
    MDLabel:  
        text: 'Screen Products'
        halign: 'center'

    MDRectangleFlatButton:  
        text: 'Contacts'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'contacts'

<ContactsScreen>:
    name: 'contacts'
    MDLabel:  
        text: 'Screen Contacts'
        halign: 'center'

    MDRectangleFlatButton:  
        text: 'Menu'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu'                    

"""
class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass 

class ProductsScreen(Screen):
    pass

class ContactsScreen(Screen):
    pass            

sm = ScreenManager()

sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))

class Lesson_14_App(MDApp):

    def build(self):
        #region Togle_Theme

        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "500"

        #endregion

        screen = Builder.load_string(screen_helper)  

        
        return screen   

Lesson_14_App().run()


