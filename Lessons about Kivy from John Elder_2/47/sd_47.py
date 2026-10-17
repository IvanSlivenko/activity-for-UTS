from kivy.lang import Builder
from kivy.properties import ColorProperty
from kivy.animation import Animation
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.utils import get_color_from_hex

from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout

from kivy.metrics import sp

class ClickableBox(ButtonBehavior, MDBoxLayout):
    pass

class MainApp(MDApp):

    data = {
        "folder": "Папка",
        "pencil": "Редагувати",
        "cog": "Налаштування",
    }

    def on_start(self):
            self.theme_cls.theme_style = "Dark"
            # self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Blue"
    
  
    def build(self):
        self.theme_cls.font_styles["Welcome"] = {
            "large": {
                "line-height": 1.2,
                "font-name": "Roboto",
                "font-size": sp(40),
            },
            "medium": {
                "line-height": 1.2,
                "font-name": "Roboto",
                "font-size": sp(36),
            },
            "small": {
                "line-height": 1.2,
                "font-name": "Roboto",
                "font-size": sp(24),
            },
        }

        root = Builder.load_file("cd_47.kv")
       

        return root

    def toggle_speed_dial(self):
        menu = self.root.ids.speed_menu
        button = self.root.ids.main_button

        if menu.opacity == 0:
            menu.opacity = 1
            menu.disabled = False
            Animation(height=dp(180), d=0.2).start(menu)
            button.icon = "close"
        else:
            anim = Animation(height=0, d=0.2)
            anim.bind(on_complete=self.hide_menu)
            anim.start(menu)
            button.icon = "plus"

    def hide_menu(self, animation, widget):
        widget.opacity = 0
        widget.disabled = True

    def menu_action(self, action):
        self.root.ids.my_label.text = action
        self.toggle_speed_dial()

MainApp().run()