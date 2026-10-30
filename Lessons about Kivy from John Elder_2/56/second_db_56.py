
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.metrics import sp
#import sqlite3
import mysql.connector


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
        #conn = sqlite3.connect("first_db_.db")
        mydb = mysql.connector.connect(
            host = "localhost", 
            user = "root",
            password = "UmanProger07092006",
            database = "second_db"

            )


        # Створення курсора
        c = mydb.cursor()

        #Create an actual database
        c.execute("CREATE DATABASE IF NOT EXISTS second_db")

        #Check to see if database was created
        #---------------------------------------
        # c.execute("SHOW DATABASES")

        # for db in c:
        #     print(db)
        #---------------------------------------



        # Створення таблиці
        c.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                name VARCHAR(100))
        """)

        #Check to see if table created
        # c.execute("SELECT *  FROM customers")
        # print(c.description)

        # # Збереження змін
        mydb.commit()

        # # Закриття з'єднання
        mydb.close()

        return Builder.load_file("first_db_56.kv")

    def submit(self):
        # Створення або підключення до бази даних
        # conn = sqlite3.connect("first_db_.db")

        mydb = mysql.connector.connect(
            host = "localhost", 
            user = "root",
            password = "UmanProger07092006",
            database = "second_db"

            )

        # Створення курсора
        c = mydb.cursor()

        #Add a Records
        sql_command = "INSERT INTO customers (name) VALUES (%s)" 
        values =  (self.root.ids.word_input.text,)

        #Execute SQL Command
        c.execute(sql_command,values)
        

        # Add a litle message    
        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'

        #Clear the input box
        self.root.ids.word_input.text = "" 


        # Збереження змін
        mydb.commit()

        # Закриття з'єднання
        mydb.close()

    def show_records(self):
         # Створення або підключення до бази даних
        # conn = sqlite3.connect("first_db_.db")

        mydb = mysql.connector.connect(
            host = "localhost", 
            user = "root",
            password = "UmanProger07092006",
            database = "second_db"

            )

        # Створення курсора
        c = mydb.cursor()

       
        #Grab records from database
        c.execute("SELECT * FROM customers ")

        records = c.fetchall()

        word = ""
        
        for record in records:
            word = f'{word}\n{record[0]}'
            self.root.ids.word_label.text = f'{word}'

        # Збереження змін
        mydb.commit()

        # Закриття з'єднання
        mydb.close()


MainApp().run()
