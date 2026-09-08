import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.spelling import Spelling



print("Spelling",Spelling)

#from kivy.uix.floatlayout import FloatLayout
#from kivy.uix.image import Image

#Set the app size
Window.size = (700,500)

Builder.load_file('spell_24.kv')



class MyLayout(Widget):
    def press(self):
        #print(self.ids.word_input.text)
        s = Spelling()
        #s.select_language('uk_UA')
        s.select_language('en_US')
        #print(s.list_languages())

        word = self.ids.word_input.text

        option = s.suggest(word)

        self.ids.word_label.text = f'Suggestions: {option}'
class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        return MyLayout()

if __name__ == "__main__":
    AwesomeApp().run()
