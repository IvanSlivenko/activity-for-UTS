import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import  ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.animation import Animation

#Set the app size
Window.size = (700,500)

Builder.load_file('animations_37.kv')

class MyLayout(Widget):

    def animate_it(self, widget, *args):
        # parameters  the animation
        animate = Animation(
            background_color=(0,0,1,1),
            duration=3)
        #Do second animation
        animate += Animation(
            size_hint=(1, 1)
        )

        # Do Third animation
        #animate += Animation(
        #    opacity=0,
        #    duration=.5)

        #Do Fo animation
        animate += Animation(
            size_hint=(.5, .5)
        )

        # Do Fi animation
        animate += Animation(
            pos_hint={"center_x": 0.1}
        )

        # Do Fia animation
        animate += Animation(
            pos_hint={"center_x": 0.5}
        )

        # Start the animation
        animate.start(widget)

        #Create a callback
        animate.bind(on_complete = self.my_callback)


    def my_callback(self, *args):
        self.ids.my_label.text="Wow Look At That!"


class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
