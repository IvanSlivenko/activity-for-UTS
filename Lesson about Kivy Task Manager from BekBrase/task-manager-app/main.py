
#region imports
from kivymd.app import MDApp

from kivymd.uix.button import MDFabButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
# from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.pickers import MDModalDatePicker

from datetime import datetime
#endregion

class DialogContent(MDBoxLayout):
    #The init function for class constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.date_text.text = datetime.now().strftime("%A %d %B %Y")

    def show_date_picker(self):
        date_dialog = MDModalDatePicker()

class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Orange"

        # return MDBoxLayout()


if __name__ == "__main__":
    app = MainApp()
    app.run()
