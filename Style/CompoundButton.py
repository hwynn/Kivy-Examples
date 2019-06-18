from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty

"""
This shows how to change the colors of buttons in kivy
And you can use custom backgrounds for buttons
"""

Builder.load_string('''
<BtnOuterFrame>:
    size_hint: (None, None)
    text: self.ourText
    width: self.texture_size[0] + 69
    height: 29
    pos: (50, 300)
    background_normal: ''
    BtnInnerFrame:
        size: (root.width, root.height)
        pos: self.parent.pos
        Button:
            size_hint: (None, 1)
            width: self.texture_size[0] + 40
            pos: (0, 0)
            color: 0, 0, 0, 1
            text: root.ourText
            background_normal: '..\imgs\BlankUpTiny.png'
            background_down: '..\imgs\BlankDownTiny.png'
            group: 'test'
        Button:
            size_hint: (None, 1)
            width: 29
            pos: (root.texture_size[0] + 40, 0)
            background_normal: '..\imgs\closeUpTiny.png'
            background_down: '..\imgs\closeDownTiny.png'
            group: 'test'

<RootWidget>:
	spacing: 5, 5
	BtnOuterFrame:
	    ourText: "Everybody Run for your lives, the train is coming!"
	BtnOuterFrame:
	BtnOuterFrame:
	BtnOuterFrame:
	BtnOuterFrame:
	BtnOuterFrame:
''')

class RootWidget(StackLayout):


    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

    def getTarget(self, p_arg):
        # gets the id of the last custom button. Used to accessing it.
        return [x for x in self.children if str(x.__class__.__name__) == p_arg]

class BtnOuterFrame(Label):
    ourText = StringProperty("")

    def __init__(self, **kwargs):
        super(BtnOuterFrame, self).__init__(**kwargs)

class BtnInnerFrame(RelativeLayout):
    ourText = StringProperty()

    def __init__(self, **kwargs):
        super(BtnInnerFrame, self).__init__(**kwargs)

class TestApp(App):

    def build(self):
        return RootWidget()



    def on_stop(self):
        print("TestApp.on_stop: finishing")
        a_frame = self.root.getTarget('BtnOuterFrame')[0]
        a_textBtn= a_frame.children[0].children[1]
        a_closeBtn = a_frame.children[0].children[0]
        print("FrameStartX:", a_frame.pos[0], end="\t\t\t")
        print("FrameEndX:", a_frame.pos[0] + a_frame.width)
        print("\tBtn1StartX:", a_textBtn.pos[0], end="\t")
        print("\tBtn1EndX:", a_textBtn.pos[0]+a_textBtn.width)
        print("\tBtn2StartX:", a_closeBtn.pos[0], end="\t")
        print("\tBtn2EndX:", a_closeBtn.pos[0]+a_closeBtn.width)
        print()
        print("Btn1WidthX:", a_textBtn.width, end="\t\t")
        print("Btn1TextureX:", a_textBtn.texture_size[0], end="\t")
        print("Btn1ExtraX:", a_textBtn.width-a_textBtn.texture_size[0])
        print()
        print("FrameWidth:", a_frame.width, end="\t\t")
        print("TotalButtonWidth:", a_textBtn.width + a_closeBtn.width)
        print("FrameBlackSpace:", a_frame.width-(a_textBtn.width + a_closeBtn.width))

if __name__ == '__main__':
    TestApp().run()