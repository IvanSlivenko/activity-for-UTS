
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
#-----------------------------------------    
    
#-----------------------------------------
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

        #-----------------------------------------------
        # root = Builder.load_file("first_db_55.kv")
        # return root
        #-----------------------------------------------
        
        #----------------------------------------------- Create or connect to db
        conn = sqlite3.connect(first_db_.db)

        #----------------------------------------------- Create a cursor
        c = coon.cursor()

        #----------------------------------------------- Create a table
        c.execute(""" CREATE TABLE if not exists customers(
                        name text)
                """)
        #------------------------------------------------ Commit Our changes
        conn.commit()

        #------------------------------------------------ Close connection
        conn.close()    

        #-----------------------------------------------    



        return Builder.load_file("first_db_55.kv")

#---------------------------------------------------
def submit(self):
        # print("Yuo clicked Submit")

    def show_records(self):
        print("Yuo clicked show_records")
#---------------------------------------------------



MainApp().run()