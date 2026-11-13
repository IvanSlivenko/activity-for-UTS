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

list_helper = """ 
Screen:
    ScrollView:
        MDList:
            id: container



"""

class Lesson_9_App(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "500"

        # Створюємо Screen та його дочірні віджети
        screen = Builder.load_string(list_helper)

        # Отримуємо MDList
        list_view = screen.ids.container

        # Наповнюємо список
        for i in range(20):

            items = ThreeLineAvatarIconListItem(
                text=f"First Name {i+1}",
                secondary_text=f"Last Name {i+1}",
                tertiary_text=f"Age {i+1}"
            )

            icon_L = IconLeftWidget(icon="android")

            icon_R = ImageRightWidget(
                source="programmer.png"
            )

            items.add_widget(icon_L)
            items.add_widget(icon_R)

            list_view.add_widget(items)

        return screen   

    # def on_start(self):
    #     for i in range(20):
    #         items = OneLineListItem(text="Item" + str(i+1))
    #         self.root.ids.container.add_widget(items)




Lesson_9_App().run()


