import sqlite3

class DataBase():
    def __init_(self):
        self.con = sqlite3.connect("task-database.db")
        self.cursor = self.con.cursor()

    #---------------------------------------- Створення таблиці
    def create_task_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXIST tasks(id integer PRIMARY KEY AUTOINCREMENT, task varchar(50)  )")
