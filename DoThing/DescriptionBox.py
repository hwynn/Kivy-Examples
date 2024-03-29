from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.properties import BooleanProperty, ObjectProperty, ListProperty
from ChangeableLabel import StretchingLabel
import SimulateOutside

Builder.load_string('''
<StretchingLabel>:
    padding: 10, 5
    size_hint_y: None
    text_size: self.width, None
    height: self.texture_size[1]
    group: 'test'
    canvas.before:
        Color:
            rgba: self.bcolor
        Rectangle:
            pos: self.pos
            size: self.size
''')

g_filename = "exampleImg.jpg"

class MyDescriptionFrame(Widget):
    c_value = StringProperty(
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \n\nProin vitae turpis ornare urna elementum pharetra non et tortor. Curabitur semper mattis viverra. \nPellentesque et lobortis purus, eu ultricies est. Nulla varius ac dolor quis mattis. Pellentesque vel accumsan tellus. Donec a nunc urna. Nulla convallis dignissim leo, tempor sagittis orci sollicitudin aliquet. Duis efficitur ex vel auctor ultricies. Etiam feugiat hendrerit mauris suscipit gravida. Quisque lobortis vitae ligula eget tristique. Nullam a nulla id enim finibus elementum eu sit amet elit.')

    def __init__(self, **kwargs):
        super(MyDescriptionFrame, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.makeLabel(), timeout=0.1)

    def makeLabel(self):
        #Before this, the stretch label doesn't exist.
        #this creates the stretching label
        c_label = StretchingLabel()
        #this makes the text of the label be equal to the c_value of this MyDescriptionFrame
        self.bind(pos=c_label.setter('pos'), width=c_label.setter('width'), c_value=c_label.setter('text'))
        #the label has a 'tempStr' property. vvv this makes an update to tempStr trigger self.setValue
        c_label.bind(tempStr=self.setValue)
        self.add_widget(c_label)
        Clock.schedule_once(lambda dt: self.chg_text(), 0.5)

    def chg_text(self):
        # this forces a property event so the label's text will be changed
        self.property('c_value').dispatch(self)

    def setValue(self, instance, p_val):
        #this is an indirect way to set MyDescriptionFrame's c_value
        #This is how StretchingLabel is able to communicate with the outside file editor
        #print("MyDescriptionFrame.setValue() instance:", instance)
        f_success = SimulateOutside.setDesc("samplefilename.jpg", p_val)
        if f_success:
            self.c_value = SimulateOutside.getDesc("samplefilename.jpg")
        else:
            print("MyDescriptionFrame.setValue() operation not successful")

Factory.register('StretchingLabel', cls=StretchingLabel)
Factory.register('MyDescriptionFrame', cls=MyDescriptionFrame)