from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput

Builder.load_string('''
<StretchDataBox>:
    size_hint_y: None
    text_size: self.width, None
    height: self.texture_size[1]
    group: 'test'
    canvas.before:
        Color:
            rgba: .7, .7, .7, 1
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
        StretchDataBox:
            text: Img_Data2.c_description
        DescDump:
            on_text_validate: Img_Data2.changeDescription(self.text)
        Label:

<ContainerBox>:
	orientation: 'horizontal'
    Button:
        text: 'h1'
        group: 'test'
    ImgData2:
''')

class StretchDataBox(Label):
    def __init__(self, **kwargs):
        super(StretchDataBox, self).__init__(**kwargs)

    def changeContents(self, value):
        print("StretchDataBox.changeContents()", value)

class DescBox(Label):
    def __init__(self, **kwargs):
        super(DescBox, self).__init__(**kwargs)

class DescDump(TextInput):
    def __init__(self, **kwargs):
        super(DescDump, self).__init__(**kwargs)
        #self.size_hint = (None, None)
        #self.size = (100, 30)
        #self.multiline = True
        self.multiline = False

    def showUs(self):
        print(self.text)
        self.text = ""

    #def on_text_validate(self):
    #    print("DescDump.on_text_validate(): ")
    #    print(self.Img_Data2)




class ImgData2(Widget):
    c_description = StringProperty('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin vitae turpis ornare urna elementum pharetra non et tortor. Curabitur semper mattis viverra. Pellentesque et lobortis purus, eu ultricies est. Nulla varius ac dolor quis mattis. Pellentesque vel accumsan tellus. Donec a nunc urna. Nulla convallis dignissim leo, tempor sagittis orci sollicitudin aliquet. Duis efficitur ex vel auctor ultricies. Etiam feugiat hendrerit mauris suscipit gravida. Quisque lobortis vitae ligula eget tristique. Nullam a nulla id enim finibus elementum eu sit amet elit.')
    def __init__(self, **kwargs):
        super(ImgData2, self).__init__(**kwargs)

    def changeDescription(self, value):
        print("ImgData2.changeDescription()", value)
        f_descBox = self.children[0].children[2]
        print(f_descBox)
        print(f_descBox.text)
        self.c_description = value
        print(f_descBox.text)

class ContainerBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)

class Nested2App(App):
    def build(self):
        return ContainerBox()
     
if __name__ == '__main__':
    Nested2App().run()