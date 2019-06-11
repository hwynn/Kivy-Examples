from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

"""
This is a demonstration of the Button widget
https://kivy.org/doc/stable/api-kivy.uix.button.html
"""

class RootWidget(GridLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Button(text='btn 1'))
        self.add_widget(Button(text='btn 2'))
        self.add_widget(Button(text='btn 3'))
        self.add_widget(Button(text='btn 4'))

class TestApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestApp().run()