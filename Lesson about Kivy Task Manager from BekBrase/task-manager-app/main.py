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
# from kivymd.uix.list import TwoLineAvatarIconListItem, ILeftBody
from kivymd.uix.list import (
    MDListItem,
    MDListItemHeadlineText,
    MDListItemSupportingText,
    MDListItemTrailingCheckbox,
)
from kivymd.uix.selectioncontrol import MDCheckbox

from dataBase import DataBase

from datetime import datetime
#endregion

db = DataBase()

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

#Class for marking for leliting the list item
#region ---------------------------------------------------class ListItemWithCheckbox var_1
# class ListItemWithCheckbox(TwoLineAvatarIconListItem):
#     def __init__(self, pk=None, **kwargs):
#         super().__init__(**kwargs)
#         self.pk = pk
#     #Markin the item complite or in complite
#     def mark(self, check, the_list_item):
#         if check.active == True:
#             the_list_item.text = '[s]'+ the_list_item.text +'[/s]'
#         else:
#             pass
#     #Deleting the list item
#     def delete_item(self, the_list_item):
#         self.parent.remove_widget(the_list_item)
#endregion

class ListItemWithCheckbox(MDBoxLayout):

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)

        self.pk = pk
        self.original_text = ""

    # Позначення виконаного завдання
    #region mark_var_1
    #--------------------------------------------------------------------------
    # def mark(self, checkbox, value):

    #     if value:
    #         self.ids.task_label.text = (
    #             f"[s]{self.original_text}[/s]"
    #         )
    #     else:
    #         # self.ids.task_label.text = self.original_text
    #         self.ids.task_label.text = db.mark_task_as_completed(value.id=pk)
    #--------------------------------------------------------------------------
    #endregion
    
    def mark(self, checkbox, active):

        if active:
            # Записуємо стан у базу
            db.mark_task_as_completed(self.pk)

            # Перекреслюємо текст
            self.ids.task_label.text = (
                f"[s]{self.original_text}[/s]"
            )

        else:
            # Оновлюємо стан у базі
            db.mark_task_as_incompleted(self.pk)

            # Повертаємо початковий текст
            self.ids.task_label.text = self.original_text
        



    # Видалення завдання
    def delete_item(self):

        if self.parent:
            self.parent.remove_widget(self)
            db.delete_task(self.pk)

class MainApp(MDApp):
    task_list_dialog = None
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

    
#endregion
#--------------------------------------------- var 3
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

#region ----------------------------------------------- add_task var_1
    # def add_task(self, task, task_date):
    #     print(task.text, task_date)
    #     self.root.ids['container'].add_widget(ListItemWithCheckbox(
    #         text='[b]'+task.text+'[/b]',
    #         secondary_text = task_date
    #         ))
    #     task.text = ""
#endregion
    
    def add_task(self, task, task_date):

        created_task = db.create_task(task.text, task_date)
        item = ListItemWithCheckbox()
        item = ListItemWithCheckbox(pk=created_task[0])

        item.original_text = f"[b]{created_task[1]}[/b]"

        item.ids.task_label.text = item.original_text
        item.ids.task_date.text = created_task[2]

        self.root.ids.container.add_widget(item)

        task.text = ""


    

    def close_dialog(self, *args):
        self.task_list_dialog.dismiss()




if __name__ == "__main__":
    app = MainApp()
    app.run()
