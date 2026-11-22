#region imports
from kivymd.app import MDApp

from kivymd.uix.button import MDFabButton
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogHeadlineText,
    MDDialogContentContainer,
)
from kivymd.uix.boxlayout import MDBoxLayout
# from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.pickers import MDModalDatePicker

from kivymd.uix.pickers.datepicker.datepicker import date

from datetime import datetime
#endregion

#region_DialogContent_var_1
# class DialogContent(MDBoxLayout):
    ##The init function for class constructor
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.ids.date_text.text = datetime.now().strftime("%A %d %B %Y")

    # def show_date_picker(self):
    #     print("show_date_picker")
    #     date_dialog = MDModalDatePicker()
    #     date_dialog.bind(on_save = self.on_save)
    #     date_dialog.open()

    # def on_save(self, instance, value, date_range):
    #     date = value.strftime("%A %d %B %Y")
    #     self.ids.date_text.text  = str(date)
        
#endregion

#------------------------------------------ var 2
class DialogContent(MDBoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = datetime.now().strftime("%A %d %B %Y")

    def show_date_picker(self):
        date_dialog = MDModalDatePicker()

        date_dialog.bind(on_ok=self.on_save)
        date_dialog.bind(on_cancel=self.on_cancel)

        date_dialog.open()

    def on_save(self, instance, *args):
        selected_dates = instance.get_date()

        if selected_dates:
            selected_date = selected_dates[0]
            self.ids.date_text.text = selected_date.strftime("%A %d %B %Y")

        instance.dismiss()

    def on_cancel(self, instance, *args):
        instance.dismiss()
#------------------------------------------------

class DialogContent_2(MDBoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def test_icon(self):
        print("Test icon")
    

    

#------------------------------------------------

class MainTestApp(MDApp):
    task_list_dialog = None
    task_list_dialog_2 = None
    def build(self):
        self.theme_cls.primary_palette = "Brown"
        # self.theme_cls.theme_style = "Light"
        self.theme_cls.theme_style = "Dark"

#region show_task_dialog_var-1-2
    #---------------------------------------------- var 1
    # def show_task_dialog(self):
    #     if not self.task_list_dialog:
    #             self.task_list_dialog = MDDialog(
    #                 title = "Create Task",
    #                 type = "custom",
    #                 content_cls = DialogContent()
    #             )

    #             self.task_list_dialog.open()
    #--------------------------------------------- var 2
    # def show_task_dialog(self):

    #     if not self.task_list_dialog:

    #         content = DialogContent()

    #         self.task_list_dialog = MDDialog(
    #             content
    #         )

    #     self.task_list_dialog.open()

    #--------------------------------------------- var 3
#endregion

    def show_task_dialog(self):

        if not self.task_list_dialog:

            content = DialogContent()

            self.task_list_dialog = MDDialog(
                MDDialogHeadlineText(
                    text="Create Task"
                ),

                MDDialogContentContainer(
                    content,
                    orientation="vertical"
                ),
            )
        self.task_list_dialog.open()

    #---------------------------------------------

    def show_task_dialog_2(self):

        if not self.task_list_dialog_2:

            content = DialogContent_2()

            self.task_list_dialog = MDDialog(
                MDDialogHeadlineText(
                    text="Create Task test"
                ),

                MDDialogContentContainer(
                    content,
                    orientation="vertical"
                ),
            )
        self.task_list_dialog.open()

    def add_task(self, task, task_date):
        print(task.text, task_date)


    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()

        


if __name__ == "__main__":
    app = MainTestApp()
    app.run()
