
from kivy.lang import Builder
from kivy.properties import ColorProperty
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.utils import get_color_from_hex
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText
from kivy.clock import Clock
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogHeadlineText,
    MDDialogContentContainer,
    MDDialogButtonContainer,
)
from kivymd.uix.label import MDLabel
from kivy.metrics import sp
# from kivymd.uix.picker import MDDatePicker
from kivymd.uix.pickers import MDModalDatePicker


class ClickableBox(ButtonBehavior, MDBoxLayout):
    pass

class MainApp(MDApp):



    def on_start(self):
            self.theme_cls.theme_style = "Dark"
            # self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Blue"
    
    def show_date_picker(self, *args):
        # self.date_dialog = MDModalDatePicker(year=2026, month=10, day=22)
        # self.date_dialog = MDModalDatePicker()
        self.date_dialog = MDModalDatePicker(mode="range")

        self.date_dialog.bind(

            on_ok=self.on_date_save,
            on_cancel=self.on_date_cancel
        )

        self.date_dialog.open()


    def on_date_save(self, date_picker, *args):
        selected_dates = date_picker.get_date()

        if selected_dates:
            if len(selected_dates) == 1:
                self.root.ids.date_label.text = (
                    selected_dates[0].strftime("%d.%m.%Y")
                )
            else:
                start_date = selected_dates[0].strftime("%d.%m.%Y")
                end_date = selected_dates[-1].strftime("%d.%m.%Y")

                self.root.ids.date_label.text = (
                    f"{start_date} - {end_date}"
                )
            
            


    def on_date_cancel(self, date_picker, *args):
        # self.root.ids.date_label.text = "You Clicked Cancel" 
        date_picker.dismiss()


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

        root = Builder.load_file("date_51.kv")
        
        return root

    

MainApp().run()