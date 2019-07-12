from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.properties import BooleanProperty
import SimulateOutside

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
            on_double_click: Img_Data2.openDescEditor()
        DescDump:
            on_text_validate: Img_Data2.updateDescription(self.text)
            on_unfocus: Img_Data2.resumeDesc()
        Label:

<ContainerBox>:
	orientation: 'horizontal'
    Button:
        text: 'h1'
        group: 'test'
    ImgData2:
''')

g_filename = "exampleImg.jpg"

class StretchDataBox(Label):
    double_click = BooleanProperty(False)
    def __init__(self, **kwargs):
        super(StretchDataBox, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        if touch.is_double_tap:
            self.double_click = not self.double_click

    def on_double_click(self, instance, p_ignoreme):
        print("StretchDataBox.on_double_click()")

class DescBox(Label):
    def __init__(self, **kwargs):
        super(DescBox, self).__init__(**kwargs)

class DescDump(TextInput):
    unfocus = BooleanProperty(False)
    validated = BooleanProperty(False)
    def __init__(self, **kwargs):
        super(DescDump, self).__init__(**kwargs)
        #self.size_hint = (None, None)
        #self.size = (100, 30)
        #self.multiline = True
        self.multiline = False
        self.size_hint_y = None
        self.height = 0

    def on_focus(self, value, p_focus):
        #this notices when a user unfocusses
        print("DescDump.on_focus() ", p_focus)
        if not p_focus:
            #we want to "resume" the description on escape
            #but not on enter. both trigger unfocus calls, so we check if this is enter
            if not self.validated:
                #we're toggling unfocus to trigger a property event
                self.unfocus = not self.unfocus
        else:
            #print('User focused')
            self.validated = False

    def on_unfocus(self, instance, p_ignoreme):
        #print("DescDump.on_unfocus() ")
        pass

    def on_text_validate(self):
        #print("DescDump.on_text_validate() ")
        self.validated = True


class ImgData2(Widget):
    c_description = StringProperty('Lorem ipsum dolor sit amet, consectetur adipiscing elit. \n\nProin vitae turpis ornare urna elementum pharetra non et tortor. Curabitur semper mattis viverra. \nPellentesque et lobortis purus, eu ultricies est. Nulla varius ac dolor quis mattis. Pellentesque vel accumsan tellus. Donec a nunc urna. Nulla convallis dignissim leo, tempor sagittis orci sollicitudin aliquet. Duis efficitur ex vel auctor ultricies. Etiam feugiat hendrerit mauris suscipit gravida. Quisque lobortis vitae ligula eget tristique. Nullam a nulla id enim finibus elementum eu sit amet elit.')
    def __init__(self, **kwargs):
        super(ImgData2, self).__init__(**kwargs)

    def openDescEditor(self):
        # shrink description box to 0 height
        f_descBox = self.children[0].children[2]
        # expand descdump to the description box's former size
        f_descDump = self.children[0].children[1]
        #but first, we want to transfer the text
        #The editor box isn't fancy, it just modifies what the description is
        f_text = f_descBox.text
        f_height = f_descBox.height
        f_descBox.text = ""
        f_descBox.height = 0
        f_descDump.text = f_text
        f_descDump.height = f_height
        pass

    def closeDescEditor(self):
        #shink descdump
        f_descDump = self.children[0].children[1]
        #expand description box
        f_descBox = self.children[0].children[2]
        pass

    def resumeDesc(self):
        #this function is similar to closeDescEditor
        #but it's called when a user unfocusses during an edit
        #rather than when they submit during an edit.
        #this function "saves" a description edit to c_description
        #without actually changing the file.
        #TODO: change color of description box to reflect unsaved changes
        f_descDump = self.children[0].children[1]
        f_descBox = self.children[0].children[2]
        f_text = f_descDump.text
        self.c_description = f_text
        f_descDump.text = ""
        f_descDump.height = 0

    def updateDescription(self, value):
        print("ImgData2.updateDescription()", value)
        f_success = SimulateOutside.setDesc(g_filename, value)
        f_descBox = self.children[0].children[2]
        #print(f_descBox)
        f_descDump = self.children[0].children[1]
        #print(f_descDump)
        if f_success:
            #clear descdump, hide descdump
            self.c_description = SimulateOutside.getDesc(g_filename)
            #print("ImgData2.updateDescription()", f_descBox.text)
            return
        else:
            self.openDescEditor()
            #print("ImgData2.updateDescription() didn't work")

class ContainerBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ContainerBox, self).__init__(**kwargs)

class Nested2App(App):
    def build(self):
        return ContainerBox()
     
if __name__ == '__main__':
    Nested2App().run()