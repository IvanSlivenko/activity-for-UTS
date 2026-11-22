from kivymd.uix.boxlayout import MDBoxLayout


class ListItemWithCheckbox(MDBoxLayout):

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)

        self.pk = pk
        self.original_text = ""

    # --------------------------------
    # Позначення завдання виконаним
    # --------------------------------

    def mark(self, checkbox, value):

        if value:
            self.ids.task_label.text = (
                f"[s]{self.original_text}[/s]"
            )
        else:
            self.ids.task_label.text = self.original_text

    # --------------------------------
    # Видалення завдання
    # --------------------------------

    def delete_item(self):

        if self.parent:
            self.parent.remove_widget(self)