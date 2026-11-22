import sqlite3

class DataBase():
    def __init_(self):
        self.con = sqlite3.connect("task-database.db")
        self.cursor = self.con.cursor()
        self.create_task_table()

    #---------------------------------------- Створення таблиці
    def create_task_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXIST tasks(id integer PRIMARY KEY AUTOINCREMENT, task varchar(50) NOT  NULL, completed  )")

    def create_task_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task VARCHAR(50) NOT NULL,
                completed BOOLEAN NOT NULL CHECK (completed IN (0,1)))
        """)

        self.con.commit()   

    #----------------------------------------- Створення завдання
    def create_task(self, task, due_date):
        self.cursor.execute("""INSERT INTO tasks(task, 
                            due_date,
                            completed,
                            VALUES(?,?,?)
                            )""", (task, due_date, 0))
        self.con.commit()                    

        #------------------------------------------------ Отримати останнє додане завдання
        created_task =  self.cursor.execute(""" SELECT id,
                                            task,
                                            due_date,
                                            FROM tasks WHERE task = ? and comleted  = 0    
                                            """, (task)).fetchall()
                                            return created_task [-1]

    #--------------------------------------------------- Отримати всі завдання
    def get_tasks(self):
        incompleted_tasks = self.cursor.execute("""
        
        """)                                        