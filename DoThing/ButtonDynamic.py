from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty
from kivy.factory import Factory

"""
We want to see how to make buttons actually do something. 
"""

#https://www.reddit.com/r/kivy/comments/86603w/assigning_functions_to_custom_widgets_outside_of/


Builder.load_string('''
<RootWidget>:
    TargetButton:
        id: targetbutton
        size_hint: (None, None)
        size: (60, 60)
        pos: (220, 220)
        background_normal: ''
        background_color: 1, 1, 1, 1
        group: 'target'        
    Button:
        text: 'A'
        size_hint: (None, None)
        size: (40, 40)
        pos: (40, 40)
        group: 'action'
    Button:
        text: 'B'
        size_hint: (None, None)
        size: (40, 40)
        pos: (100, 40)
        group: 'action'
    Button:
        text: 'L'
        size_hint: (None, None)
        size: (20, 40)
        pos: (160, 40)
        group: 'move'
        on_press: targetbutton.shiftTargetPos(3)
    Button:
        text: 'R'
        size_hint: (None, None)
        size: (20, 40)
        pos: (220, 40)
        group: 'move'
        on_press: targetbutton.shiftTargetPos(1)
    Button:
        text: 'U'
        size_hint: (None, None)
        size: (40, 20)
        pos: (180, 80)
        group: 'move'
        on_press: targetbutton.shiftTargetPos(0)
    Button:
        text: 'D'
        size_hint: (None, None)
        size: (40, 20)
        pos: (180, 20)
        group: 'move'
        on_press: targetbutton.shiftTargetPos(2)
    Button:
        text: 'R^'
        size_hint: (None, None)
        size: (40, 20)
        pos: (260, 70)
        group: 'color'
        on_press: targetbutton.shiftTargetCol(0)
    Button:
        text: 'G^'
        size_hint: (None, None)
        size: (40, 20)
        pos: (320, 70)
        group: 'color'
        on_press: targetbutton.shiftTargetCol(1)
    Button:
        text: 'B^'
        size_hint: (None, None)
        size: (40, 20)
        pos: (380, 70)
        group: 'color'
        on_press: targetbutton.shiftTargetCol(2)
    Button:
        text: 'Rv'
        size_hint: (None, None)
        size: (40, 20)
        pos: (260, 30)
        group: 'color'
        on_press: targetbutton.shiftTargetCol(3)
    Button:
        text: 'Gv'
        size_hint: (None, None)
        size: (40, 20)
        pos: (320, 30)
        group: 'color'
        on_press: targetbutton.shiftTargetCol(4)
    Button:
        text: 'Bv'
        size_hint: (None, None)
        size: (40, 20)
        pos: (380, 30)
        group: 'color'
        on_press: targetbutton.shiftTargetCol(5)
''')

class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

class TargetButton(Button):
    bcolor = ListProperty([1, 1, 1, 1])

    def __init__(self, **kwargs):
        super(TargetButton, self).__init__(**kwargs)

    def on_press(self):
        print('you pressed it!')
        return True
    def on_release(self):
        print()
        return True

    def shiftTargetPos(self, p_num):
        f_x, f_y = self.pos
        if p_num > 3 or p_num < 0:
            return True
        if p_num == 0:
            f_y = f_y + 5;
        elif p_num == 1:
            f_x = f_x + 5;
        elif p_num == 2:
            if f_y>=5:
                f_y = f_y - 5;
        elif p_num == 3:
            if f_x >= 5:
                f_x = f_x - 5;
        self.pos = (f_x, f_y)
        return True

    def shiftTargetCol(self, p_num):
        f_r, f_g, f_b, f_a = self.background_color
        if p_num > 5 or p_num < 0:
            return True
        if p_num == 0:
            if f_r <= 0.9:
                f_r = f_r + 0.1;
        elif p_num == 1:
            if f_g <= 0.9:
                f_g = f_g + 0.1;
        elif p_num == 2:
            if f_b <= 0.9:
                f_b = f_b + 0.1;
        elif p_num == 3:
            if f_r >= 0.1:
                f_r = f_r - 0.1;
        elif p_num == 4:
            if f_g >= 0.1:
                f_g = f_g - 0.1;
        elif p_num == 5:
            if f_b >= 0.1:
                f_b = f_b - 0.1;
        self.background_color = (f_r, f_g, f_b, f_a)
        return True


class TestApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestApp().run()