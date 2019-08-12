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
    padding: 10, 6
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

<ContainerBox>:
    orientation: 'horizontal'
    GridLayout:
        cols: 1
        row_force_default: False
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

#--------------Debugging functions---------------------

def showMaybeText(p_widget):
    #prints text of widget if widget has text
    try: print(p_widget.text)
    except: print()

def heightScan(p_widget, p_level):
    #prints height of all widgets in the tree. used for debugging
    for i_child in reversed(list(p_widget.children)):
        print('\t' * p_level, i_child, end='')
        showMaybeText(i_child)
        print('\t' * p_level, "height: ", i_child.height)
        heightScan(i_child, p_level + 1)

def assess_widget(p_widget):
    #this is a function that will determine the total size and position of items INSIDE a widget
    #this is used for debugging
    #Note: this has a bug with calculating absolute positions in nested wigdets
    #return: ((x position, y position),(x size/width, y size/height))
    f_max_x = None
    f_max_y = None
    f_min_x = None
    f_min_y = None
    try:
        for i_child in reversed(list(p_widget.children)):
            if f_max_x==None:
                f_max_x = i_child.pos[0]+i_child.width
            elif (i_child.pos[0]+i_child.width) > f_max_x:
                f_max_x = i_child.pos[0] + i_child.width
            if f_max_y==None:
                f_max_y = i_child.pos[1]+i_child.height
            elif (i_child.pos[1]+i_child.height) > f_max_y:
                f_max_y = i_child.pos[1]+i_child.height
            if f_min_x==None:
                f_min_x = i_child.pos[0]
            elif i_child.pos[0] < f_min_x:
                f_min_x = i_child.pos[0]
            if f_min_y==None:
                f_min_y = i_child.pos[1]
            elif i_child.pos[1] < f_min_y:
                f_min_y = i_child.pos[1]
        #return (position, size)
        return ((f_min_x,f_min_y),((f_max_x-f_min_x),(f_max_y-f_min_y)))
    except:
        return ((p_widget.pos[0],p_widget.pos[1]),(p_widget.width, p_widget.height))

def boundryScan(p_widget, p_level):
    #prints height of all widgets in the tree. used for debugging
    for i_child in reversed(list(p_widget.children)):
        print('\t' * p_level, i_child, end='')
        showMaybeText(i_child)
        print('\t' * p_level, assess_widget(i_child))
        boundryScan(i_child, p_level + 1)

#--------------kivy classes----------------------

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

class ContainerBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)
        #Debugging statements
        #Clock.schedule_once(lambda dt: heightScan(self, 0), timeout=4)
        #Clock.schedule_once(lambda dt: boundryScan(self, 0), timeout=4)

class Nested2App(App):
    def build(self):
        return ContainerBox()

if __name__ == '__main__':
    Nested2App().run()