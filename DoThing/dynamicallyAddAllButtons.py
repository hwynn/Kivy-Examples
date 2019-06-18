from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty
from kivy.factory import Factory
from kivy.properties import DictProperty

"""
We're now adding buttons dynamically.
We add the first button dynamically. So we have to change the way we access it.
"""

#https://stackoverflow.com/questions/56587838/access-dynamically-added-widget-with-id

Builder.load_string('''
<RootWidget>:  
    Button:
        text: 'Add'
        size_hint: (None, None)
        size: (40, 40)
        pos: (40, 40)
        group: 'action'
        on_press: root.createNextTarget()
    Button:
        text: 'res'
        size_hint: (None, None)
        size: (40, 40)
        pos: (100, 40)
        group: 'action'
        on_press: root.resetTarget()
    Button:
        text: 'L'
        size_hint: (None, None)
        size: (20, 40)
        pos: (160, 40)
        group: 'move'
        on_press: root.dynamic_ids['targetbutton0'].shiftTargetPos(3)
    Button:
        text: 'R'
        size_hint: (None, None)
        size: (20, 40)
        pos: (220, 40)
        group: 'move'
        on_press: root.dynamic_ids['targetbutton0'].shiftTargetPos(1)
    Button:
        text: 'U'
        size_hint: (None, None)
        size: (40, 20)
        pos: (180, 80)
        group: 'move'
        on_press: root.dynamic_ids['targetbutton0'].shiftTargetPos(0)
    Button:
        text: 'D'
        size_hint: (None, None)
        size: (40, 20)
        pos: (180, 20)
        group: 'move'
        on_press: root.dynamic_ids['targetbutton0'].shiftTargetPos(2)
    Button:
        text: 'R^'
        size_hint: (None, None)
        size: (40, 20)
        pos: (260, 70)
        group: 'color'
        on_press: root.dynamic_ids['targetbutton0'].shiftTargetCol(0)
    Button:
        text: 'G^'
        size_hint: (None, None)
        size: (40, 20)
        pos: (320, 70)
        group: 'color'
        on_press: root.dynamic_ids['targetbutton0'].shiftTargetCol(1)
    Button:
        text: 'B^'
        size_hint: (None, None)
        size: (40, 20)
        pos: (380, 70)
        group: 'color'
        on_press: root.dynamic_ids['targetbutton0'].shiftTargetCol(2)
    Button:
        text: 'Rv'
        size_hint: (None, None)
        size: (40, 20)
        pos: (260, 30)
        group: 'color'
        on_press: root.dynamic_ids['targetbutton0'].shiftTargetCol(3)
    Button:
        text: 'Gv'
        size_hint: (None, None)
        size: (40, 20)
        pos: (320, 30)
        group: 'color'
        on_press: root.dynamic_ids['targetbutton0'].shiftTargetCol(4)
    Button:
        text: 'Bv'
        size_hint: (None, None)
        size: (40, 20)
        pos: (380, 30)
        group: 'color'
        on_press: root.dynamic_ids['targetbutton0'].shiftTargetCol(5)
''')

class RootWidget(FloatLayout):
    dynamic_ids = DictProperty({})  # declare class attribute, dynamic_ids

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        #note: self.ids isn't populated yet. We can't use it yet.
        self.createNextTarget()

    def targetIntel(self):
        f_target = self.dynamic_ids['targetbutton0']
        print("position:\t",f_target.pos)
        print("color:\t",f_target.background_color)
        return True #I'm still not 100% certain why we add this

    def resetTarget(self):
        f_target = self.dynamic_ids['targetbutton0']
        f_target.pos = (80, 220)
        f_target.background_color = (0.7, 0.7, 0.7, 1.0)
        return True
    
    def countTargets(self):
        #print(str(self.children[-1].__class__.__name__)) #this is how to get an object type as a string!
        return [str(x.__class__.__name__) for x in self.children if x != None].count('TargetButton')

    def createNextTarget(self):
        #dynamically add new button
        f_id = "targetbutton" + str(self.countTargets())
        f_nextposX = 80 + (10 + 60) * self.countTargets()
        f_nextposY = 220
        f_nextsizeX = 60
        f_nextsizeY = 60
        f_nextButton = TargetButton(id=f_id ,
                               text="btn"+str(self.countTargets()),
                               size_hint=(None, None),
                               pos=(f_nextposX, f_nextposY),
                               size=(f_nextsizeX, f_nextsizeY),
                               background_normal = '',
                               background_color=(0.7, 0.7, 0.7, 1.0),
                               group = 'target')
        self.add_widget(f_nextButton)
        self.dynamic_ids[f_id] = f_nextButton
        f_nextButton.bind(on_press=TargetButton.lowerAllRGB)

class TargetButton(Button):
    bcolor = ListProperty([0.7, 0.7, 0.7, 1.0])

    def __init__(self, **kwargs):
        super(TargetButton, self).__init__(**kwargs)

    def on_press(self):
        print('you pressed it!')
        return True
    def on_release(self):
        return True

    def shiftTargetPos(self, p_num):
        f_x, f_y = self.pos
        if p_num > 3 or p_num < 0:
            return True
        if p_num == 0:
            f_y = f_y + 5
        elif p_num == 1:
            f_x = f_x + 5
        elif p_num == 2:
            if f_y>=5:
                f_y = f_y - 5
        elif p_num == 3:
            if f_x >= 5:
                f_x = f_x - 5
        self.pos = (f_x, f_y)
        return True

    def shiftTargetCol(self, p_num):
        f_r, f_g, f_b, f_a = self.background_color
        if p_num > 5 or p_num < 0:
            return True
        if p_num == 0:
            if f_r <= 0.9:
                f_r = f_r + 0.1
        elif p_num == 1:
            if f_g <= 0.9:
                f_g = f_g + 0.1
        elif p_num == 2:
            if f_b <= 0.9:
                f_b = f_b + 0.1
        elif p_num == 3:
            if f_r >= 0.1:
                f_r = f_r - 0.1
        elif p_num == 4:
            if f_g >= 0.1:
                f_g = f_g - 0.1
        elif p_num == 5:
            if f_b >= 0.1:
                f_b = f_b - 0.1
        self.background_color = (f_r, f_g, f_b, f_a)
        return True

    def lowerAllRGB(self):
        f_r, f_g, f_b, f_a = self.background_color
        if f_r >= 0.1:
            f_r = f_r - 0.1
        if f_g >= 0.1:
            f_g = f_g - 0.1
        if f_b >= 0.1:
            f_b = f_b - 0.1
        self.background_color = (f_r, f_g, f_b, f_a)
        return True

class TestApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestApp().run()