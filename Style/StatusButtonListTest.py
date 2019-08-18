from kivy.app import App
from kivy.lang import Builder
from functools import partial
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import OptionProperty, ListProperty, NumericProperty
from kivy.uix.behaviors import ToggleButtonBehavior


Builder.load_string('''
<StatusButtonList>:
    size_hint: None, None
    size: 250, 250
<StatusButton>:
    size_hint: None, None
    size: 50, 50
<Controller>:
    orientation: 'vertical'
    StatusButtonList:
''')


class StatusButton(Button):
    status = OptionProperty('off', options=('off', 'on'))

    def __init__(self, p_val, **kwargs):
        super(StatusButton, self).__init__(**kwargs)
        self.c_val = p_val #each button has an int value that will be used in callbacks
        self.background_normal = '..\imgs\starOff.png'
        self.background_down = '..\imgs\starOffDown.png'

    def on_status(self, widget, value):
        #print("StatusButton.on_status()", widget, value)
        if value == 'on':
            self.background_normal = '..\imgs\starOn.png'
            self.background_down = '..\imgs\starOnDown.png'
        else:
            self.background_normal = '..\imgs\starOff.png'
            self.background_down = '..\imgs\starOffDown.png'

class StatusButtonList(BoxLayout):
    number = NumericProperty(0)
    buttonList = ListProperty()

    def __init__(self, **kwargs):
        super(StatusButtonList, self).__init__(**kwargs)
        for i in range(5):
            i_button = StatusButton(p_val=i+1)
            self.add_widget(i_button)
            self.buttonList.append(i_button)
            i_callback = partial(self.set_number)
            i_button.bind(on_press=i_callback)

    def set_number(self, p_button):
        #print("StatusButtonList.set_number()", p_button, p_button.c_val)
        #each button has a different stored value.
        # So number is set to the value of whatever button is pressed
        self.number = p_button.c_val
        #External functions used here

    def on_number(self, instance, value):
        #print("StatusButtonList.on_number()", instance, value)
        for i in range(value):
            self.buttonList[i].status = 'on'
        for i in range(value,5):
            self.buttonList[i].status = 'off'


class Controller(BoxLayout):
    def __init__(self, **kwargs):
        super(Controller, self).__init__(**kwargs)


class SampleApp(App):
    def build(self):
        return Controller()


SampleApp().run()
