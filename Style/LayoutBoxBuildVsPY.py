"""
This is a demonstration of how widgets are displayed in
the 'BoxLayout' in Kivy
This example shows how load_string() can be used and
how to achieve identical results the "normal" way
"""



from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.lang import Builder


"""
Builder.load_string('''
<Demo>:


    BoxLayout:
        orientation: 'vertical'
        Button:
            size_hint_x: 0.4
            pos_hint: {'x': 0}
            text: 'pos_hint: x=0'

        Button:
            size_hint_x: 0.2
            pos_hint: {'center_x': 0.5}
            text: 'pos_hint: center_x=0.5'

        Button:
            size_hint_x: 0.4
            pos_hint: {'right': 1}
            text: 'pos_hint: right=1'

''')
"""

class Demo(BoxLayout):
    #"""
    def __init__(self, **kwargs):
        super(Demo, self).__init__(**kwargs)
        self.orientation='vertical'
        button1 = Button(size_hint_x= 0.4,
                        pos_hint={'x': 0},
                        text='pos_hint: x=0')
        button2 = Button(size_hint_x= 0.2,
                        pos_hint={'center_x': 0.5},
                        text='pos_hint: center_x=0.5')
        button3 = Button(size_hint_x= 0.4,
                        pos_hint={'right': 1},
                        text='pos_hint: right=1')
        self.add_widget(button1)
        self.add_widget(button2)
        self.add_widget(button3)
    #"""
    pass


class DemoApp(App):
    def build(self):
        return Demo()


if __name__ == '__main__':
    DemoApp().run()
