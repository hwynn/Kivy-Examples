from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

"""
This is a demonstration of how property names work in kivy.
We have custom button. This button had a property named 'pressed'
'pressed' sounds like a reserved keyword in kivy. Is it?
We misspelled it 'paressed' (which could never be a reserved keyword) and tested
if we could get that to work the same way.
The property 'paressed' absolutely works. So we do have freedom choosing property names in kivy
"""



class RootWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text='btn 1'))
        cb = CustomBtn()
        cb.bind(paressed=self.btn_pressed)  #notice we use the property name here as well
        self.add_widget(cb)
        self.add_widget(Button(text='btn 2'))

    def btn_pressed(self, instance, p_pos):
        print('RootWidget:\tbtn_pressed()')
        print('\tpos: {x}'.format(x=p_pos))

class CustomBtn(Widget):
    paressed = ListProperty([0, 0])          #we declare a pressed property. so on_pressed will be called
                                            #if the value of this changes.
                                            #there's a lot of heavy reliance on variable names in kivy.

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):  #if the touch falls inside our widget
            self.paressed = touch.pos
            # we consumed the touch. return False here to propagate
            # the touch further to the children.
            print()
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    def on_pressed(self, instance, p_pos):    #the name of this function must reflect property it's tied to
        print('CustomBtn:\ton_pressed()')   #Note that this never runs because the property is called
        print('\tpos: {x}'.format(x=p_pos)) #'paressed' instead of 'pressed'

    def on_paressed(self, instance, p_pos):   #but this made up function will be called instead
        print("CustomBtn:\ton_paressed()")       #because the name matches 'paressed'
        print("\tyou spelled it wrong")

class TestApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestApp().run()