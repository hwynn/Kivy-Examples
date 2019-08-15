from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.properties import BooleanProperty, ObjectProperty
#GreyLabel will be dynamically added to MyFrame inside the first ResizingRow
Builder.load_string('''
<GreyLabel>:
    height: 30
    canvas.before:
        Color:
            rgba: .7, .7, .7, 1
        Rectangle:
            pos: self.pos
            size: self.size

<Resizing_GridLayout@GridLayout>:
    cols: 1
    row_force_default: True
    #foo: [self.rows_minimum.update({i: x.height}) for i, x in enumerate(reversed(list(self.children)))]
<ResizingRow_GridLayout@GridLayout>:
    cols: 1
    height: sum([c.height for c in self.children])

<ContainerBox>:
    orientation: 'horizontal'

    Resizing_GridLayout:
        ResizingRow_GridLayout:
            id: Row1
            MyFrame:
                id: TitleContent
        ResizingRow_GridLayout:
            id: Row2
            Label:
                height: 30
                text: 'Label One'
            TextInput:
                height: 30
                multiline: False
                write_tab: False
                hint_text: 'Insert one liner'

        ResizingRow_GridLayout:
            id: Row3
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
''')
class GreyLabel(Label):
    def __init__(self, **kwargs):
        super(GreyLabel, self).__init__(**kwargs)

class Resizing_GridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(Resizing_GridLayout, self).__init__(**kwargs)
        self.foo = [self.rows_minimum.update({i: x.height}) for i, x in enumerate(reversed(list(self.children)))]

class ResizingRow_GridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(ResizingRow_GridLayout, self).__init__(**kwargs)


class MyFrame(Widget):
    c_value = StringProperty('SomeThing goes here')

    def __init__(self, **kwargs):
        super(MyFrame, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.makeLabel(), timeout=0.1)

    def makeLabel(self):
        c_label = GreyLabel()
        self.bind(pos=c_label.setter('pos'), width=c_label.setter('width'), c_value=c_label.setter('text'))
        self.add_widget(c_label)
        # this forces a property event so the label's text will be changed
        Clock.schedule_once(lambda dt: self.property('c_value').dispatch(self), 0.5)
        # this forces a property event so the label's pos will be changed
        Clock.schedule_once(lambda dt: self.chg_text(c_label), 1)

    def chg_text(self, p_widget):
        # this forces a property event so the label's text will be changed
        self.property('c_value').dispatch(self)
        self.height = p_widget.height

class ContainerBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)

class Nested2App(App):
    def build(self):
        return ContainerBox()

    def on_stop(self):
        print()
        print("Nested2App.on_start: starting")
        f_Resizing_Grid = self.root.children[0]
        f_Resizing_Row = self.root.children[0].children[2]
        f_MyFrame = self.root.children[0].children[2].children[0]
        f_FreshLabel = f_MyFrame.children[0]
        print("\tf_Resizing_Grid size: \t", f_Resizing_Grid.size, "\t\theight:", f_Resizing_Grid.size[1])
        print("\tf_Resizing_Grid pos : \t\t", f_Resizing_Grid.pos)
        print("\tf_Resizing_Row size: \t", f_Resizing_Row.size, "\t\theight:", f_Resizing_Row.size[1])
        print("\tf_Resizing_Row pos : \t\t", f_Resizing_Row.pos)
        print("\tf_MyFrame size: \t\t", f_MyFrame.size, "\t\theight:", f_MyFrame.size[1])
        print("\tf_MyFrame pos : \t\t\t", f_MyFrame.pos)
        print("\tf_FreshLabel size: \t\t", f_FreshLabel.size, "\t\theight:", f_FreshLabel.size[1])
        print("\tf_FreshLabel pos : \t\t\t", f_FreshLabel.pos)


if __name__ == '__main__':
    Nested2App().run()