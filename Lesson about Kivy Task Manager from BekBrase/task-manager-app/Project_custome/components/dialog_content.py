from datetime import datetime

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.pickers import MDModalDatePicker


class DialogContent(MDBoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ids.date_text.text = datetime.now().strftime(
            "%A %d %B %Y"
        )

    # --------------------------------
    # Відкриття календаря
    # --------------------------------

    def show_date_picker(self):

        date_dialog = MDModalDatePicker()

        date_dialog.bind(on_ok=self.on_save)
        date_dialog.bind(on_cancel=self.on_cancel)

        date_dialog.open()

    # --------------------------------
    # Збереження вибраної дати
    # --------------------------------

    def on_save(self, instance, *args):

        selected_dates = instance.get_date()

        if selected_dates:

            selected_date = selected_dates[0]

            self.ids.date_text.text = (
                selected_date.strftime("%A %d %B %Y")
            )

        instance.dismiss()

    # --------------------------------
    # Скасування вибору дати
    # --------------------------------

    def on_cancel(self, instance, *args):

        instance.dismiss()