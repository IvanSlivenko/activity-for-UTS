#region imports
from kivymd.app import MDApp

from kivymd.uix.button import MDFabButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
# from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.pickers import MDModalDatePicker

from kivymd.uix.pickers.datepicker.datepicker import date

from datetime import datetime
#endregion

class DialogContent(MDBoxLayout):
    #The init function for class constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = datetime.now().strftime("%A %d %B %Y")

    def show_date_picker(self):
        date_dialog = MDModalDatePicker()
        date_dialog.bind(on_save = self.on_save)

    def on_save(self, instance, value, date_range):
        date = value.strtime("%A %d %B %Y")
        self.ids.date_text.text  = str(date)
        


class MainApp(MDApp):
    task_list_dialog = None
    def build(self):
        self.theme_cls.primary_palette = "Orange"

    def show_task_function(self):
        if not self.task_list_dialog:
                self.task_list_dialog = MDDialog(
                    title = "Create Task",
                    type = "custome",
                    contetnt_cls = DialogContent()
                )

                self.task_list_dialog.open()

    def add_task(self, task, task_date):
        print(task.text, task_date)




    def close_dialog(self, **kwargs):
        self.task_list_dialog.dismiss()

        


if __name__ == "__main__":
    app = MainApp()
    app.run()
