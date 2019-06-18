from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty
from kivy.factory import Factory
from kivy.properties import DictProperty, NumericProperty
from kivy.clock import Clock
from functools import partial

"""
This one lets you add and remove buttons dynamically.
"""

#https://www.reddit.com/r/kivy/comments/86603w/assigning_functions_to_custom_widgets_outside_of/


Builder.load_string('''
<RootWidget>:  
    Button:
        text: 'add'
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
        text: 'Show'
        size_hint: (None, None)
        size: (40, 40)
        pos: (160, 40)
        group: 'action'
        on_press: root.showTargets()
''')

class RootWidget(FloatLayout):
    dynamic_ids = DictProperty({})  # declare class attribute, dynamic_ids

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.c_startX = 80
        self.createNextTarget()

    def countTargets(self):
        # counts how many custom buttons exist
        return [str(x.__class__.__name__) for x in self.children if x != None].count('TargetButton')

    def closeTarget(self, p_targetID):
        #removes a dynamically added button. This is a big deal!
        #careful way to remove key from dictionary
        try:
            f_target = self.dynamic_ids[p_targetID]
            print("RootWidget.closeTarget(): closing", p_targetID)
            if f_target != None:
                self.remove_widget(f_target)
                del self.dynamic_ids[p_targetID]
        except KeyError:
            print("RootWidget.closeTarget(): key not in dictionary. Weird")
        return True

    def showTargets(self):
        print("RootWidget.showTargets()")
        print([str(x.text) for x in self.children if str(x.__class__.__name__) == 'TargetButton'])

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
        f_nextButton.bind(on_press=self.scheduleThing)
        #print("RootWidget.createNextTarget()", self.dynamic_ids)

    def scheduleThing(self, arg):
        #without lambda here, this would pass the timeout arguement to our function.
        Clock.schedule_once(lambda dt: self.closeTarget(arg.id), timeout=0.01)
        #print("RootWidget.scheduleThing():", arg, type(arg))
        #print("RootWidget.scheduleThing():", arg.id)


class TargetButton(Button):
    def __init__(self, **kwargs):
        super(TargetButton, self).__init__(**kwargs)

    def lowerAllRGB(self):
        #makes the button slightly darker
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