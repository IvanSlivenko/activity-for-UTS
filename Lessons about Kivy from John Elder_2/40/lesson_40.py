import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


#Set the app size
Window.size = (700,500)

Builder.load_file('switch_40.kv')

class MyLayout(Widget):
    def switch_click(self, switchObject, switchValue):
        #print(switchValue)
        if(switchValue):
            self.ids.my_label.text="You clicked the Switch On!"
        else:
            self.ids.my_label.text = "You clicked the Switch OFF!"
            self.ids.my_switch.disabled=True


class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
