from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.properties import BooleanProperty, ObjectProperty, ListProperty
import SimulateOutside

Builder.load_string('''
<StretchingLabel>:
    size_hint_y: None
    text_size: self.width, None
    padding: 10, 5
    height: self.texture_size[1]
    group: 'test'
    canvas.before:
        Color:
            rgba: self.bcolor
        Rectangle:
            pos: self.pos
            size: self.size


<ImgData2>:
    id: Img_Data2
	BoxLayout:
		orientation: 'vertical'
		size: root.size
		pos: root.pos
		Label:
			text: 'Description'
			size_hint_y: None
			height: 30
			bold: True
        StretchingLabel:
        Label:

<ContainerBox>:
	orientation: 'horizontal'
    Button:
        text: 'h1'
        group: 'test'
    ImgData2:
''')

g_filename = "exampleImg.jpg"

class StretchingLabel(Label):
    bcolor = ListProperty([.7, .7, .7, 1])
    edit = BooleanProperty(False)
    tempStr = c_description = StringProperty("")
    textinput = ObjectProperty(None, allownone=True)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and not self.edit:
            self.edit = True
        return super(StretchingLabel, self).on_touch_down(touch)

    def on_edit(self, instance, value):
        if not value:
            if self.textinput:
                self.remove_widget(self.textinput)
            return
        self.textinput = t = TextInput(
                text=self.text, size_hint=(None, None),
                font_size=self.font_size, font_name=self.font_name,
                pos=self.pos, size=self.size, multiline=False)
        self.bind(pos=t.setter('pos'), size=t.setter('size'))
        self.add_widget(self.textinput)
        t.bind(on_text_validate=self.on_text_validate, focus=self.on_text_focus)

    def on_text_validate(self, instance):
        print("StretchingLabel.on_text_validate() new text:", instance.text)
        self.tempStr = instance.text
        self.edit = False

    def on_text_focus(self, instance, focus):
        if focus is False:
            self.tempStr = instance.text
            self.edit = False

    def neutralizeColor(self):
        print("StretchingLabel.neutralizeColor()")
        self.bcolor = (.7, .7, .7, 1)
        pass

    def agitateColor(self):
        print("StretchingLabel.agitateColor()")
        self.bcolor = (0.7, 0, 0, 1)

class ImgData2(Widget):
    c_description = StringProperty(
        'Lorem ipsum dolor sit amet, consectetur adipiscing elit. \n\nProin vitae turpis ornare urna elementum pharetra non et tortor. Curabitur semper mattis viverra. \nPellentesque et lobortis purus, eu ultricies est. Nulla varius ac dolor quis mattis. Pellentesque vel accumsan tellus. Donec a nunc urna. Nulla convallis dignissim leo, tempor sagittis orci sollicitudin aliquet. Duis efficitur ex vel auctor ultricies. Etiam feugiat hendrerit mauris suscipit gravida. Quisque lobortis vitae ligula eget tristique. Nullam a nulla id enim finibus elementum eu sit amet elit.')

    def __init__(self, **kwargs):
        super(ImgData2, self).__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.makeLabel(), timeout=0.1)

    def testTime(self):
        print("ImgData2.testTime(): loaded from clock")

    def makeLabel(self):
        c_label = StretchingLabel()
        self.bind(pos=c_label.setter('pos'), width=c_label.setter('width'), c_description=c_label.setter('text'))
        c_label.bind(tempStr=self.setDescription)

        self.add_widget(c_label)

        Clock.schedule_once(lambda dt: self.chg_text(), 0.5)

    def chg_text(self):
        #this forces a property event so the label's text will be changed
        self.property('c_description').dispatch(self)

    def setDescription(self, instance, val):
        print("ImgData2.setDescription() instance:", instance)
        print("ImgData2.setDescription() val:", val)
        self.c_description = val

    def on_parent(self, instance, value):
        print("ImgData2.on_parent()")


class ContainerBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)


class Nested2App(App):
    def build(self):
        return ContainerBox()


if __name__ == '__main__':
    Nested2App().run()