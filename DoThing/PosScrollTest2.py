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
from lib.modules.adaptive_grid_layout import Adaptive_GridLayout

#This is a scrolltest with more of a user interface inside rather than a bunch of labels

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
            size: self.size
            Adaptive_GridLayout:
                id: layout_content
                cols: 1
                grow_rows: True
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                ResizingFrame:
                    id: Row1
                    cols: 1
                    grow_rows: True
                Label:
                    height: 30
                    text: 'Label One'
                    canvas.before:
                        Color:
                            rgba: .4, .4, .4, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size
                TextInput:
                    height: 30
                    multiline: False
                    write_tab: False
                    hint_text: 'Insert one liner'
                Label:
                    height: 45
                    text: 'Label two'
                Button:
                    text: 'Button One'
                    height: 60
                GridLayout:
                    rows: 1
                    height: 25
                    Button:
                        text: 'Button Two'
                    Button:
                        text: 'Button three'
                Label:
                    height: 20
                    text: "Lorem ipsum dkdsjahf lkasjkat"
                Label:
                    height: 20
                    text: "Lorem ipsdodo dod dodo do dodt"
                Label:
                    height: 20
                    text: "Lorem ipsdkjwww  ww woij ksdsdf sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
                Label:
                    height: 20
                    text: "Lorem ipsum dolor sit amet"
''')

class ResizingFrame(Adaptive_GridLayout):
    c_value = StringProperty('SomeThing goes here')
    def __init__(self, **kwargs):
        super(ResizingFrame, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.makeLabel(), timeout=0.1)

    def makeLabel(self):
        c_label = StretchingLabel()
        self.bind(pos=c_label.setter('pos'), width=c_label.setter('width'), c_value=c_label.setter('text'))
        self.add_widget(c_label)
        # this forces a property event so the label's text will be changed
        Clock.schedule_once(lambda dt: self.property('c_value').dispatch(self), 0.5)
        # this forces a property event so the label's pos will be changed
        Clock.schedule_once(lambda dt: self.chg_text(c_label), 1)
        Clock.schedule_once(lambda dt: self.trigger_refresh_y_dimension(), 1.5)

    def chg_text(self, p_widget):
        # this forces a property event so the label's text will be changed
        self.property('c_value').dispatch(self)
        #Note: This just seems to push the label down from the top of the screen without changing the layout's height
        self.trigger_refresh_y_dimension()
        #the same behaviour can be seen if you double click the stretching label and enter a change

    def on_height(self, instance, value):
        print("ResizingFrame.on_height()", self.height)



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
