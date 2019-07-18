from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

Builder.load_string('''
<StretchingLabel>:
    color: 0, 0, 0, 1   # black color text
    size_hint_y: None
    text_size: self.width, None
    height: self.texture_size[1]   
    group: 'test'
    canvas.before:
        Color:
            rgba: .7, .7, .7, 1
        Rectangle:
            pos: self.pos
            size: self.size

<MyLabelFrame>:
    id: xLabel

<ContainerBox>:
    orientation: 'horizontal'
    Button:
        text: 'h1'
        group: 'test'

    BoxLayout:
        orientation: 'vertical'
        size: root.size
        pos: root.pos

        Label:
            text: 'Description'
            size_hint_y: None
            height: 30
            bold: True

        MyLabelFrame:

        Label:
''')


class StretchingLabel(Label):

    def __init__(self, **kwargs):
        super(StretchingLabel, self).__init__(**kwargs)
        # This is for debugging
        Clock.schedule_once(lambda dt: print("StretchingLabel.init(): ", self.text), timeout=0.01)

    def on_double_click(self, instance, p_ignoreme):
        # This is also for debugging
        print("StretchingLabel.on_double_click():", self.text)

    def on_parent(self, instance, value):
        print("StretchingLabel.on_parent()")


class MyLabelFrame(Widget):
    c_description = StringProperty(
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \n\nProin vitae turpis ornare urna elementum pharetra non et tortor. Curabitur semper mattis viverra. \nPellentesque et lobortis purus, eu ultricies est. Nulla varius ac dolor quis mattis. Pellentesque vel accumsan tellus. Donec a nunc urna. Nulla convallis dignissim leo, tempor sagittis orci sollicitudin aliquet. Duis efficitur ex vel auctor ultricies. Etiam feugiat hendrerit mauris suscipit gravida. Quisque lobortis vitae ligula eget tristique. Nullam a nulla id enim finibus elementum eu sit amet elit.')

    def __init__(self, **kwargs):
        super(MyLabelFrame, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.makeLabel(), timeout=0.1)

    def testTime(self):
        print("MyLabelFrame.testTime(): loaded from clock")

    def makeLabel(self):
        c_label = StretchingLabel()
        self.bind(pos=c_label.setter('pos'), width=c_label.setter('width'), c_description=c_label.setter('text'))
        self.add_widget(c_label)

        Clock.schedule_once(lambda dt: self.chg_text(), 0.5)

    def chg_text(self):
        #this forces a property event so the label's text will be changed
        self.property('c_description').dispatch(self)

    def on_parent(self, instance, value):
        print("MyLabelFrame.on_parent()")

    def on_double_click(self, instance, p_ignoreme):
        # This is also for debugging
        print("MyLabelFrame.on_double_click():", self.text)

class ContainerBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)


class Nested2App(App):
    def build(self):
        return ContainerBox()


if __name__ == '__main__':
    Nested2App().run()