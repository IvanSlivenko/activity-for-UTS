
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.metrics import sp
import sqlite3


class ClickableBox(ButtonBehavior, MDBoxLayout):
    pass


class MainApp(MDApp):

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

        # Створення або підключення до бази даних
        conn = sqlite3.connect("first_db_.db")

        # Створення курсора
        c = conn.cursor()

        # Створення таблиці
        c.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                name TEXT
            )
        """)

        # Збереження змін
        conn.commit()

        # Закриття з'єднання
        conn.close()

        return Builder.load_file("first_db_55.kv")

    def submit(self):
        # Створення або підключення до бази даних
        conn = sqlite3.connect("first_db_.db")

        # Створення курсора
        c = conn.cursor()

        #Add a Records
        c.execute("INSERT INTO customers VALUES (:first)",
            {
                'first': self.root.ids.word_input.text
            })

        # Add a litle message    
        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'

        #Clear the input box
        self.root.ids.word_input.text = "" 


        # Збереження змін
        conn.commit()

        # Закриття з'єднання
        conn.close()

    def show_records(self):
         # Створення або підключення до бази даних
        conn = sqlite3.connect("first_db_.db")

        # Створення курсора
        c = conn.cursor()

       
        #Grab records from database
        c.execute("SELECT * FROM customers ")

        records = c.fetchall()

        word = ""
        
        for record in records:
            word = f'{word}\n{record}'
            self.root.ids.word_label.text = f'{word}'

        # Збереження змін
        conn.commit()

        # Закриття з'єднання
        conn.close()


MainApp().run()
