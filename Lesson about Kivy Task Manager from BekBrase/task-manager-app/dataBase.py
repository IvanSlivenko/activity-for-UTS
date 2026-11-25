import sqlite3

class DataBase():
    def __init__(self):
        self.con = sqlite3.connect("task-database.db")
        self.cursor = self.con.cursor()
        self.create_task_table()

        self.update_task_table()

        # columns = self.cursor.execute(
        # "PRAGMA table_info(tasks)"
        # ).fetchall()

        # for column in columns:
        #     print(column)

    #---------------------------------------- Створення таблиці
    # def create_task_table(self):
    #     self.cursor.execute("CREATE TABLE IF NOT EXIST tasks(id integer PRIMARY KEY AUTOINCREMENT, task varchar(50) NOT  NULL, completed  )")

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
        self.cursor.execute("""INSERT INTO tasks(task, due_date, completed)
                            VALUES(?,?,?)
                            """, (task, due_date, 0))
        self.con.commit()                    

        #------------------------------------------------ Отримати останнє додане завдання
        created_task =  self.cursor.execute(""" 
                                            SELECT id, task, due_date 
                                            FROM tasks 
                                            WHERE task = ? and completed  = 0 """, (task,)).fetchone()
        # return created_task[-1]
        return created_task

    #--------------------------------------------------- Отримати всі завдання
    def get_tasks(self):
        
        incompleted_tasks = self.cursor.execute("""
                                                SELECT id, task, due_date 
                                                FROM tasks 
                                                WHERE completed = 0 """).fetchall()
        
        completed_tasks = self.cursor.execute("""
                                                SELECT id, task, due_date 
                                                FROM tasks 
                                                WHERE completed = 1 """).fetchall() 
                                                
        return incompleted_tasks, completed_tasks

    #--------------------------------------------------- Оновити завдання


    def mark_task_as_completed(self, task_id):
        self.cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))                                           
        self.con.commit()


    #region ----------------------------------------------------------- mark_task_as_incompleted var 1 
    # def mark_task_as_incompleted(self, task_id):
    #     self.cursor.execute("UPDATE tasks SET completed = 0 WHERE id = ?", (task_id,))                                           
    #     self.con.commit()

    #     task_text = self.cursor.execute("SELECT task FROM tasks WHERE id = ?", (task_id,)).fetchall()
    #     return task_text[0][0]
    #endregion

    def mark_task_as_incompleted(self, task_id):
        self.cursor.execute("""
            UPDATE tasks
            SET completed = 0
            WHERE id = ?
        """, (task_id,))

        self.con.commit() 

   

    def update_task_table(self):

        columns = self.cursor.execute(
            "PRAGMA table_info(tasks)"
        ).fetchall()

        column_names = [column[1] for column in columns]

        if "due_date" not in column_names:
            self.cursor.execute(
                "ALTER TABLE tasks ADD COLUMN due_date TEXT"
            )

        self.con.commit()

    #-------------------------------------------------- Видалити завдання
    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))

        # print(f"ID для видалення: {task_id}")
        # print(f"Видалено записів: {self.cursor.rowcount}")

        self.con.commit()

    #------------------------------------------------------------------------------ Вихід зі з'єднання

    def close_db_connection(self):
        self.con.close()


    

