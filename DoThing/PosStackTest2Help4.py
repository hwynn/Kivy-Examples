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
from lib.modules.adaptive_grid_layout import Adaptive_GridLayout
#This now has StretchingLabel, which will change size to match it's dynamically changing contents
#ResizingFrame is derived from the new class Adaptive_GridLayout.
#So this adaptive layout itself is dynamically adding StretchingLabel
Builder.load_string('''
<StretchingLabel>:
    padding: 10, 5
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
<Resizing_GridLayout>:
    cols: 1
    row_force_default: True
<ResizingRow_GridLayout>:
    cols: 1
    height: sum([c.height for c in self.children])

<ContainerBox>:
    orientation: 'horizontal'

    Resizing_GridLayout:
        ResizingFrame:
            id: Row1
            cols: 1
            grow_rows: True
        Adaptive_GridLayout:
            id: Row2
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

        Adaptive_GridLayout:
            id: Row3
            cols: 1
            grow_rows: True
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

class StretchingLabel(Label):
    edit = BooleanProperty(False)
    textinput = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super(StretchingLabel, self).__init__(**kwargs)
        #self.size_hint_y = None

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and touch.is_double_tap and not self.edit:
            self.edit = True
        return super(StretchingLabel, self).on_touch_down(touch)

    def on_edit(self, instance, value):
        if not value:
            if self.textinput:
                self.remove_widget(self.textinput)
            return
        self.textinput = t = TextInput(
            text=self.text, size_hint=(None, None),
            font_size=self.font_size, font_name=self.font_name,
            pos=self.pos, size=self.size, multiline=False)
        self.bind(pos=t.setter('pos'), size=t.setter('size'))
        self.add_widget(self.textinput)
        t.bind(on_text_validate=self.on_text_validate, focus=self.on_text_focus)

    def on_text_validate(self, instance):
        self.text = instance.text
        self.edit = False
        print(self, type(self))
        print(self.parent, type(self.parent))
        #Note: This is the child widget calling the layout's function that should adjust its height
        self.parent.trigger_refresh_y_dimension()

    def on_text_focus(self, instance, focus):
        if focus is False:
            self.text = instance.text
            self.edit = False

    def on_height(self, instance, value):
        print("StretchingLabel.on_height()", self.height)

class Resizing_GridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(Resizing_GridLayout, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.calc_height(), timeout=0.1)

    def calc_height(self):
        foo = [self.rows_minimum.update({i: x.height}) for i, x in enumerate(reversed(list(self.children)))]

    def on_height(self, instance, value):
        print("Resizing_GridLayout.on_height()", self.height)

class ResizingRow_GridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(ResizingRow_GridLayout, self).__init__(**kwargs)

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
        f_ResizingFrame = self.root.children[0].children[2]
        f_FreshLabel = f_ResizingFrame.children[0]
        print("\tf_Resizing_Grid size: \t", f_Resizing_Grid.size, "\t\theight:", f_Resizing_Grid.height)
        print("\tf_Resizing_Grid rmin: \t\t", f_Resizing_Grid.rows_minimum)
        print("\tf_Resizing_Grid pos: \t\t", f_Resizing_Grid.pos)

        print("\tf_ResizingFrame size: \t\t", f_ResizingFrame.size, "\t\theight:", f_ResizingFrame.height)
        print("\tf_ResizingFrame rmin: \t\t", f_ResizingFrame.rows_minimum)
        print("\tf_ResizingFrame padding: \t\t", f_ResizingFrame.padding)
        print("\tf_ResizingFrame pos: \t\t\t", f_ResizingFrame.pos)

        print("\tf_FreshLabel size: \t\t", f_FreshLabel.size, "\t\theight:", f_FreshLabel.height)
        print("\tf_FreshLabel padding: \t\t", f_FreshLabel.padding)
        print("\tf_FreshLabel pos: \t\t\t", f_FreshLabel.pos)


if __name__ == '__main__':
    Nested2App().run()