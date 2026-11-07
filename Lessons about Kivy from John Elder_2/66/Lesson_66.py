from kivy.metrics import sp
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import MDListItemHeadlineText


class MainApp(MDApp):

    def on_start(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"

    def presser(self, pressed, list_id):
        self.root.ids[list_id].text = f"You pressed {list_id}"

        

    def build(self):

        self.theme_cls.font_styles["Welcome"] = {
            "large": {
                "line-height": 1.2,
                "font-name": "Roboto",
                "font-size": sp(40),
            },
            "medium": {
                "line-height": 1.2,
                "font-name": "Roboto",
                "font-size": sp(36),
            },
            "small": {
                "line-height": 1.2,
                "font-name": "Roboto",
                "font-size": sp(24),
            },
        }

    
        return Builder.load_file("Lesson_66.kv")

    

    

MainApp().run()