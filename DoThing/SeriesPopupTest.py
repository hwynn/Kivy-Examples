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
from SeriesPopupButton import SeriesButton, SeriesPopup

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
        popup_trigger = SeriesButton()
        self.top_label1 = ColorLabel(size_hint_y=None, height=50, text=popup_trigger.seriesName, bcolor=[.3, .7, .5, 1])
        self.top_label2 = ColorLabel(size_hint_y=None, height=50, bcolor=[.6, .3, .4, 1])
        if popup_trigger.seriesIns==-1:
            self.top_label2.text = ""
        else:
            self.top_label2.text=str(popup_trigger.seriesIns)
        # this detects changes in the series values and calls changes to the user interface be made
        popup_trigger.bind(seriesName=self.top_label1.setter('text'))
        popup_trigger.bind(seriesIns=self.update_installment)
        self.add_widget(self.top_label1)
        self.add_widget(self.top_label2)
        self.add_widget(popup_trigger)

    def update_installment(self, instance, value):
        # this function updates the installment number shown on the user interface whenever the value changes
        if value == -1: #this implies no series exists, thus no number should be displayed
            self.top_label2.text = ""
        else:
            self.top_label2.text = str(value)

class SampleApp(App):
    def build(self):
        return RootWidget()


SampleApp().run()