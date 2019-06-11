from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty


"""
This is a demonstration of how events tied to properties work in kivy.
In exPropertyBinding.py, we showed how these properties work in general.
Upon a property update, an event tied to that property is triggered.
We have methods tied to 'pressed' in the root widget and the custom button.
Watch when everything happens once the middle button is pressed.
"""

class RootWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Button(text='btn 1'))
        cb = CustomBtn()
        # function bound to 'pressed' outside the class that the 'pressed' property was defined
        cb.bind(pressed=self.btn_pressed)

        self.add_widget(cb)
        self.add_widget(Button(text='btn 2'))

    def btn_pressed(self, instance, pos):
        print("btn_pressed()")
        print('pos: printed from root widget: {pos}'.format(pos=pos))
        print('we also have a thing: {x}'.format(x=instance.c_thing))

class CustomBtn(Widget):
    pressed = ListProperty([0, 0])

    c_thing = 5
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos        #we update the value of the property, which calls on_pressed()
            #on_pressed() is called here.
            #so this function gets interupted here
            #but for some reason, btn_pressed() is also called before this
            self.c_thing = 38
            print('other thing is {x}'.format(x=self.c_thing))
            # we consumed the touch. return False here to propagate
            # the touch further to the children.
            return False
        return super(CustomBtn, self).on_touch_down(touch)

    # function bound to 'pressed' within the class that the 'pressed' property was defined
    def on_pressed(self, instance, pos):
        print("on_pressed()")
        print('pressed at {pos}'.format(pos=pos))


class TestApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestApp().run()