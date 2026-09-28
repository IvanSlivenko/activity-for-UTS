import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window


#Set the app size
Window.size = (700,500)

Builder.load_file('progres_37.kv')

class MyLayout(Widget):
    def press_it(self):
        #Get Current value ProgressBar
        current = self.ids.my_progress_bar.value

        # If statement to start over after 100
        if current == 1:
            current = 0

        #Increment value by .25
        current += .25

        #Update ProgressBar
        self.ids.my_progress_bar.value = current

        #Update The label
        self.ids.my_label.text = f'{int(current*100)}% Progress'





class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
