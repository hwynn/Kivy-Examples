from kivy.app import App
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import OptionProperty, ListProperty, NumericProperty
from kivy.uix.behaviors import ToggleButtonBehavior

Builder.load_string('''
<StatusButton>:
    size_hint: None, None
    size: 50, 50
<Controller>:
    orientation: 'vertical'
    StatusButton:
''')


class StatusButton(Button):
    status = OptionProperty('off', options=('off', 'on'))

    def __init__(self, **kwargs):
        super(StatusButton, self).__init__(**kwargs)
        self.background_normal = '..\imgs\starOff.png'
        self.background_down = '..\imgs\starOffDown.png'

    def on_status(self, widget, value):
        if value == 'on':
            self.background_normal = '..\imgs\starOn.png'
            self.background_down = '..\imgs\starOnDown.png'
        else:
            self.background_normal = '..\imgs\starOff.png'
            self.background_down = '..\imgs\starOffDown.png'


class Controller(BoxLayout):
    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)


class SampleApp(App):
    def build(self):
        return Controller()


SampleApp().run()
