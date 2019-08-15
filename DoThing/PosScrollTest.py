from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.properties import BooleanProperty, ObjectProperty, ListProperty
from ChangeableLabel0 import StretchingLabel
from PrevNext import NextPrevBar
import SimulateOutside

#this shows off how to properly use scrollview

Builder.load_string('''    
<Controller>:
    layout_content: layout_content
    BoxLayout:
        id: bl
        orientation: 'vertical'
        padding: 10, 10
        row_default_height: '48dp'
        row_force_default: True
        spacing: 10, 10
        ScrollView:
            scroll_type: ['bars']
            bar_width: 6
            size: self.size
            GridLayout:
                id: layout_content
                size_hint_y: None
                cols: 1
                row_default_height: '20dp'
                row_force_default: True
                spacing: 0, 0
                padding: 0, 0

                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    text: "Lorem ipsum dolor sit amet"

''')

class Controller(FloatLayout):
    layout_content=ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)
        self.layout_content.bind(minimum_height=self.layout_content.setter('height'))

class Nested2App(App):
    def build(self):
        return Controller()

if __name__ == '__main__':
    Nested2App().run()
