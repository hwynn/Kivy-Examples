from kivy.app import App
from kivy.lang import Builder
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout

Builder.load_string('''
<AnchorWidget>:
	AnchorLayout:
		anchor_x: 'right'
		anchor_y: 'center'
		size: root.size
		pos: root.pos
		Button:
			text: 'This is anchor layout'
			size_hint: (.5, .20)
			group: 'test'
		Button:
			text: 'right center'
			size_hint: (.20, .5)
			group: 'test'


<FloatWidget>:
    FloatLayout:
        size: root.size
		pos: root.pos
		Button:
			text: 'pos_hint=x:0, y:0\\nsize_hint=(.5, .20)'
			size_hint: (.5, .20)
			pos_hint: {'x': .0, 'y': .0}
			group: 'test'
		Button:
			text: 'pos_hint=x:2, y:45\\nsize_hint=(.3, .5)'
			size_hint: (.3, .5)
			pos_hint: {'x': .2, 'y': .45}
			group: 'test'
		Button:
			text: 'pos_hint=x:5, y:0\\nsize_hint=(.5, .20)'
			size_hint: (.5, .20)
			pos_hint: {'x': .5, 'y': .0}
			group: 'test'
		Button:
			text: 'pos_hint=x:2, y:2\\npos_hint(.2, .20)'
			size_hint: (.2, .20)
			pos_hint: {'x': .2, 'y': .2}
			group: 'test'


<ContainerBox>:
	orientation: 'vertical'
	AnchorWidget:
	FloatWidget:
''')


class AnchorWidget(Widget):
    def __init__(self, **kwargs):
        super(AnchorWidget, self).__init__(**kwargs)

class FloatWidget(Widget):
    def __init__(self, **kwargs):
        super(FloatWidget, self).__init__(**kwargs)

class ContainerBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)

class Nested2App(App):
    def build(self):
        return ContainerBox() 
     
if __name__ == '__main__':
    Nested2App().run()