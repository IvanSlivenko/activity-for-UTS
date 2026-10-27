
from kivy.lang import Builder
from kivy.properties import ColorProperty
from kivy.animation import Animation
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
# from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.pickers import MDTimePickerDialVertical
from kivymd.uix.pickers import MDTimePickerInput
from datetime import datetime
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView

class ClickableBox(ButtonBehavior, MDBoxLayout):
    pass

class MainApp(MDApp):

    def on_start(self):
            self.theme_cls.theme_style = "Dark"
            # self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_palette = "Blue"
#-----------------------------------------    


#-----------------------------------------
    def build(self):
        
        screen = Screen()

        row_data = [
            ("Jhon", "Elder", "UmanProger@urk.net", "067 470 87 19"),
            ("Forest", "Gamp", "UmanProger@urk.net", "067 470 87 20"),
            ("Ivan", "Slivenko", "UmanProger@urk.net", "067 470 87 21"),
            ("John", "Smith", "john.smith@example.com", "067 470 87 22"),
            ("Anna", "Johnson", "anna.johnson@example.com", "067 470 87 23"),
            ("Peter", "Brown", "peter.brown@example.com", "067 470 87 24"),
            ("Olena", "Kovalenko", "olena.kovalenko@example.com", "067 470 87 25"),
            ("Michael", "Wilson", "michael.wilson@example.com", "067 470 87 26"),
            ("Sofia", "Miller", "sofia.miller@example.com", "067 470 87 27"),
            ("David", "Taylor", "david.taylor@example.com", "067 470 87 28"),
            ("James", "Anderson", "james.anderson@example.com", "067 470 87 29"),
            ("Emma", "Thomas", "emma.thomas@example.com", "067 470 87 30"),
            ("Daniel", "Jackson", "daniel.jackson@example.com", "067 470 87 31"),
            ("Olivia", "White", "olivia.white@example.com", "067 470 87 32"),
            ("Robert", "Harris", "robert.harris@example.com", "067 470 87 33"),
            ("Maria", "Martin", "maria.martin@example.com", "067 470 87 34"),
            ("William", "Thompson", "william.thompson@example.com", "067 470 87 35"),
            ("Natalie", "Garcia", "natalie.garcia@example.com", "067 470 87 36"),
            ("Alexander", "Martinez", "alexander.martinez@example.com", "067 470 87 37"),
            ("Victoria", "Robinson", "victoria.robinson@example.com", "067 470 87 38"),
            ("Thomas", "Clark", "thomas.clark@example.com", "067 470 87 39"),
            ("Kateryna", "Shevchenko", "kateryna.shevchenko@example.com", "067 470 87 40"),
            ("Andrew", "Lewis", "andrew.lewis@example.com", "067 470 87 41"),
            ("Yulia", "Walker", "yulia.walker@example.com", "067 470 87 42"),
            ("Matthew", "Hall", "matthew.hall@example.com", "067 470 87 43"),
            ("Dmytro", "Bondarenko", "dmytro.bondarenko@example.com", "067 470 87 44"),
            ("Elizabeth", "Allen", "elizabeth.allen@example.com", "067 470 87 45"),
            ("Serhii", "Tkachenko", "serhii.tkachenko@example.com", "067 470 87 46"),
            ("Christopher", "Young", "christopher.young@example.com", "067 470 87 47"),
            ("Anastasia", "Melnyk", "anastasia.melnyk@example.com", "067 470 87 48"),
        ]

        # Додаємо порядковий номер на початок кожного рядка
        row_data = [
            (number, *row)
            for number, row in enumerate(row_data, start=1)
        ]

        table = MDDataTable(
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=(0.9, 0.6),
            check=True,
            use_pagination=True,
            rows_num=4,
            pagination_menu_height="360dp",
            pagination_menu_pos = "auto",

            background_color=get_color_from_hex("#ffffff80"),
             # Фон заголовка
            background_color_header=get_color_from_hex("#313131"),

            # Фон комірок
            background_color_cell=get_color_from_hex("#424242"),

            # Фон виділеної комірки
            background_color_selected_cell=get_color_from_hex("#1565C0"),
            
            column_data=[
                ("№", dp(20)),
                ("First Name", dp(30)),
                ("Last Name", dp(30)),
                ("Email Address", dp(50)),
                ("Phone Number", dp(30)),
            ],
            row_data=row_data,
        )

        # Збільшуємо товщину смуг прокрутки
        def set_scrollbar_width(widget):
            if isinstance(widget, ScrollView):
                widget.bar_width = dp(12)

            for child in widget.children:
                set_scrollbar_width(child)

        set_scrollbar_width(table)
        #-----------------------------------------------
        table.bind(on_check_press=self.checked)
        table.bind(on_row_press=self.row_checked)

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

    

        # root = Builder.load_file("table_54.kv")
        
        # return root

        screen.add_widget(table)
        return screen

    def checked(self, instance_table, current_row):
        print(instance_table, current_row)

    def row_checked(self, instance_table, instance_row):    
        print(instance_table, instance_row)

MainApp().run()