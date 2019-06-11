from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

"""
This is a demonstration of how widgets are displayed in
the 'FloatLayout' in Kivy
This first example will be super simple.
"""


class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        """
        self.add_widget(Button(size=(500, 200),
                        pos=(0, 0),
                        text='btn 1'))
        self.add_widget(Button(size=(300, 500),
                        pos=(200, 20),
                        text='btn 2'))
        self.add_widget(Button(size_hint=(.5, .20),
                        pos=(20, 200),
                        text='btn 3'))
        self.add_widget(Button(size_hint=(.5, .20),
                        pos=(200, 200),
                        text='btn 4'))
        """
        self.add_widget(Button(size_hint=(.5, .20),     #size is 50% of the window width and 20% of the window height
                        pos_hint={'x': .0, 'y': .0},    #position is displaced by 0% x and 0%y
                        text='btn 1'))
        self.add_widget(Button(size_hint=(.3, .5),      #size is 30% of the window width and 50% of the window height
                        pos_hint={'x': .2, 'y': .45},   #position is displaced by 20% x and 45%y
                        text='btn 2'))
        self.add_widget(Button(size_hint=(.5, .20),     #size is 50% of the window width and 20% of the window height
                        pos_hint={'x': .5, 'y': .0},    #position is halfway up the window, and touching the left side
                        text='btn 3'))
        self.add_widget(Button(size_hint=(.2, .20),
                        pos_hint={'x': .2, 'y': .2},    #a fifth of the way up the window, a fifth right of the window
                        text='btn 4'))
        #"""
class TestApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestApp().run()