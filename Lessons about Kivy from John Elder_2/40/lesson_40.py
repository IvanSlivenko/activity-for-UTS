import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp


#Set the app size
Window.size = (700,500)

Builder.load_file('testing_40.kv')

Builder.load_string("""
<MyCard>
    padding: "4dp"
    size_hint_y: None
    height: "100dp"

    MDRelativeLayout:

        MDIconButton:
            icon: "dots-vertical"
            pos_hint: {"top": 1, "right": 1}
            focus_behavior: False

        MDLabel:
            id: label
            text: root.text
            adaptive_size: True
            color: "grey"
            pos: "12dp", "12dp"
            bold: True
""")

class MyLayout(Widget):
    pass


class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
