from kivy.app import App
from kivy.lang import Builder
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

Builder.load_string('''
<HBoxWidget>:
	BoxLayout:
		size: root.size
		pos: root.pos
		id: boxlayout_h
		orientation: 'horizontal'
		Button:
			text: 'This is BoxLayout'
			group: 'test'
		Button:
			text: 'orientation: \\'horizontal\\''
			group: 'test'

<VBoxWidget>:
	BoxLayout:
		orientation: 'vertical'
		size: root.size
		pos: root.pos
		Button:
			text: 'This is also BoxLayout'
			group: 'test'
		Button:
			text: 'orientation: \\'vertical\\''
			group: 'test'

<Grid3Widget>:
    GridLayout:
        cols: 3
        size: root.size
		pos: root.pos
		Button:
			text: 'This is GridLayout'
			group: 'test'
		Button:
			text: 'cols: 3'
			group: 'test'
		Button:
			text: 'btn 3'
			group: 'test'
		Button:
			text: 'btn 4'
			group: 'test'
		Button:
			text: 'btn 5'
			group: 'test'

<Grid4Widget>:
    GridLayout:
        cols: 4
        size: root.size
		pos: root.pos
		Button:
			text: 'This is GridLayout'
			group: 'test'
		Button:
			text: 'cols: 4'
			group: 'test'
		Button:
			text: 'btn 3'
			group: 'test'
		Button:
			text: 'btn 4'
			group: 'test'
		Button:
			text: 'btn 5'
			group: 'test'

<ContainerBox>:
	orientation: 'vertical'
	HBoxWidget:
	VBoxWidget:
	Grid3Widget:
	Grid4Widget:
''')


class HBoxWidget(Widget):
    def __init__(self, **kwargs):
        super(HBoxWidget, self).__init__(**kwargs)

class VBoxWidget(Widget):
    def __init__(self, **kwargs):
        super(VBoxWidget, self).__init__(**kwargs)

class Grid3Widget(Widget):
    def __init__(self, **kwargs):
        super(Grid3Widget, self).__init__(**kwargs)

class Grid4Widget(Widget):
    def __init__(self, **kwargs):
        super(Grid4Widget, self).__init__(**kwargs)

class ContainerBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)

class Nested2App(App):
    def build(self):
        return ContainerBox() 
     
if __name__ == '__main__':
    Nested2App().run()