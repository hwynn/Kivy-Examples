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

# GreyLabel will be dynamically added to ResizingFrame inside the first ResizingRow
# ResizingFrame is derived from the new class Adaptive_GridLayout.
# So this adaptive layout itself is dynamically adding GreyLabel
Builder.load_string('''
<GreyLabel>:
    size_hint_y: None

    height: 30

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

def showMaybeText(p_widget):
    #prints text of widget if widget has text
    try: print(p_widget.text, end='')
    except: pass

def heightScan(p_widget, p_level):
    #prints height of all widgets in the tree. used for debugging
    for i_child in reversed(list(p_widget.children)):
        print('\t' * p_level, end='')
        print(i_child, end='')
        showMaybeText(i_child)
        print()
        print('\t' * p_level, end='')
        print("height: ", i_child.height)
        heightScan(i_child, p_level + 1)

def assess_widget(p_widget):
    #this is a recursive function that will determine the total size and position of items inside a widget
    #this is also used for debugging
    #Note: this has a bug with calculating absolute positions in nested wigdets
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
        print('\t' * p_level, end='')
        print(i_child, end='')
        showMaybeText(i_child)
        print()
        print('\t' * p_level, assess_widget(i_child))
        boundryScan(i_child, p_level + 1)


class GreyLabel(Label):

    def __init__(self, **kwargs):
        super(GreyLabel, self).__init__(**kwargs)
        #self.padding = (10, 10)


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
        c_label = GreyLabel()
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
        # Note: This just seems to push the label down from the top of the screen without changing the layout's height
        self.trigger_refresh_y_dimension()
        # the same behaviour can be seen if you double click the stretching label and enter a change


class ContainerBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: boundryScan(self, 0), timeout=4)


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