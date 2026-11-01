

# from kivy.config import Config
# Config.set('graphics', 'position', 'custom')
# Config.set('graphics', 'left', 1110)
# Config.set('graphics', 'top', 400)



from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.metrics import sp
from kivy.core.window import Window

from kivy.uix.floatlayout import FloatLayout
from kivy_garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

import matplotlib.pyplot as plt

#----------------------------
# x = [1,2,3,4,5]
# y = [5, 12, 6, 9, 15]

# plt.plot(x,y)
# plt.ylabel("Y Axis")
# plt.xlabel("X Axis")
#----------------------------

x = [1, 2, 3, 4, 5]
y = [5, 12, 6, 9, 15]

fig, ax = plt.subplots()

ax.plot(x, y)
ax.set_ylabel("Y Axis")
ax.set_xlabel("X Axis")


class Matty(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # box = self.ids.box
        # box.add_widget(FigureCanvasKivyAgg)

        self.canvas_widget = FigureCanvasKivyAgg(fig)
        self.canvas_widget.size_hint = (1, 1)
        self.canvas_widget.pos_hint = {"x": 0, "y": 0}

        self.add_widget(self.canvas_widget)

    def save_it(self):
        pass


class MainApp(MDApp):

    def on_start(self):
        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

    def build(self):
        # Window.borderless = True
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

 

        return Builder.load_file("Lesson_59.kv")






MainApp().run()
