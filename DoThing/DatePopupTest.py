from datetime import datetime
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, NumericProperty, ListProperty
import SimulateOutside
from DatePopupButton import DateEditButton, DatePopup

Builder.load_string('''
<ColorLabel>:
    canvas.before:
        Color:
            rgba: self.bcolor
        Rectangle:
            pos: self.pos
            size: self.size

<RootWidget>:
    orientation: 'vertical'
''')
class ColorLabel(Label):
    bcolor = ListProperty([.7, .7, .7, 1])

    def __init__(self, **kwargs):
        super(ColorLabel, self).__init__(**kwargs)
        pass
        # this is a label with color. I don't know if this custom class is needed
        # there's probably a way to not use this


class RootWidget(BoxLayout):
    # this user interface is just a small part of what would be in a larger user interface
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        # all of this stuff will need to be added into whatever user interface you use
        popup_trigger = DateEditButton()
        self.top_label0 = ColorLabel(size_hint_y=None, height=50,
                                     bcolor=[.6, .3, .4, 1])
        if popup_trigger.hasDate:
            self.top_label0.text=str(datetime.strptime(popup_trigger.ISODateString, "%Y-%m-%dT%H:%M:%S"))
        else:
            self.top_label0.text="No date given"
        # this detects changes in the series values and calls changes to the user interface be made
        popup_trigger.bind(ISODateString=self.update_date)
        self.add_widget(self.top_label0)
        self.add_widget(popup_trigger)

    def update_date(self, instance, value):
        # this function updates the installment number shown on the user interface whenever the value changes
        self.top_label0.text = str(datetime.strptime(value, "%Y-%m-%dT%H:%M:%S"))


class SampleApp(App):
    def build(self):
        return RootWidget()


SampleApp().run()