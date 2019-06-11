from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

"""
This shows how to change the colors of buttons in kivy
And you can use custom backgrounds for buttons
"""

Builder.load_string('''
<StretchButtons>:
    FloatLayout:
        size: root.size
		pos: root.pos
		Button:
			text: 'btn 1'
			size_hint: (.2, .20)
			pos_hint: {'x': .1, 'y': .4}
			background_normal: 'white.png'
			group: 'test'
		Button:
			text: 'btn 2'
			size_hint: (.2, .20)
			pos_hint: {'x': .4, 'y': .4}
			background_down: ''
			group: 'test'
		Button:
			text: 'btn 3'
			size_hint: (.2, .20)
			pos_hint: {'x': .7, 'y': .4}
			background_normal: ''
			background_color: 1, .3, .4, .85
			group: 'test'

<RigidButtons>:
    FloatLayout:
        size: root.size
		pos: root.pos
		Button:
		    size_hint_x: None
		    size_hint_y: None
            width: 92
            height: 25
            pos: (100, 50)
			background_normal: '..\imgs\startNormal1.png'
			background_down: '..\imgs\startDown2.png'
			group: 'test'
		Button:
		    size_hint_x: None
		    size_hint_y: None
            size: (92, 25)
            pos: (200, 50)
			background_normal: '..\imgs\startNormal1.png'
			background_down: '..\imgs\startDown2.png'
			group: 'test'
		Button:
		    size_hint: (None, None)
            size: (92, 25)
            pos: (300, 50)
			background_normal: '..\imgs\startNormal1.png'
			background_down: '..\imgs\startDown2.png'
			group: 'test'

<RootWidget>:
	orientation: 'vertical'
	StretchButtons:
	RigidButtons:

''')

class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

class StretchButtons(Widget):
    def __init__(self, **kwargs):
        super(StretchButtons, self).__init__(**kwargs)

class RigidButtons(Widget):
    def __init__(self, **kwargs):
        super(RigidButtons, self).__init__(**kwargs)

class TestApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestApp().run()