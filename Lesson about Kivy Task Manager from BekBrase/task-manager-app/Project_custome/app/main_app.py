from pathlib import Path

from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.dialog import (
    MDDialog,
    MDDialogHeadlineText,
    MDDialogContentContainer,
)

from components.task_item import ListItemWithCheckbox
from components.dialog_content import DialogContent
from screens.main_screen import MainScreen


class MainApp(MDApp):

    task_list_dialog = None
#-----------------------------------------------------------
    # def build(self):

    #     self.theme_cls.primary_palette = "Brown"
    #     self.theme_cls.theme_style = "Dark"

    #     kv_file = (
    #         Path(__file__).resolve().parent.parent
    #         / "kv"
    #         / "main.kv"
    #     )

    #     return Builder.load_file(str(kv_file))
#------------------------------------------------------------
    def build(self):

        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.theme_style = "Dark"

        kv_dir = Path(__file__).resolve().parent.parent / "kv"

        # Завантаження компонентів
        Builder.load_file(
            str(kv_dir / "components" / "task_item.kv"),
            rulesonly=True
        )

        Builder.load_file(
            str(kv_dir / "components" / "dialog_content.kv"),
            rulesonly=True
        )

        # Завантаження головного екрана
        Builder.load_file(
            str(kv_dir / "screens" / "main_screen.kv"),
            rulesonly=True
        )

        # Завантаження кореневого віджета
        return Builder.load_file(
            str(kv_dir / "main.kv")
        )
    # --------------------------------
    # Відкриття діалогового вікна
    # --------------------------------

    def show_task_dialog(self):

        if not self.task_list_dialog:

            self.dialog_content = DialogContent()

            self.task_list_dialog = MDDialog(

                MDDialogHeadlineText(
                    text="Create Task"
                ),

                MDDialogContentContainer(
                    self.dialog_content,
                    orientation="vertical"
                ),
            )

        self.task_list_dialog.open()

    # --------------------------------
    # Додавання завдання
    # --------------------------------

    def add_task(self, task, task_date):

        task_text = task.text.strip()

        if not task_text:
            return

        item = ListItemWithCheckbox()

        item.original_text = f"[b]{task_text}[/b]"

        item.ids.task_label.text = item.original_text
        item.ids.task_date.text = task_date

        self.root.ids.container.add_widget(item)

        task.text = ""

    # --------------------------------
    # Закриття діалогового вікна
    # --------------------------------

    def close_dialog(self, *args):

        if self.task_list_dialog:
            self.task_list_dialog.dismiss()