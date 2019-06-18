from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, DictProperty
from kivy.factory import Factory
#https://stackoverflow.com/questions/2349991/how-to-import-other-python-files
from DynamicButtonList import DynamicTagList

"""
This is an example of using our custom class from another file
to dynamically create and close buttons
"""

class RootWidget(GridLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.cols = 3
        f_taglist = DynamicTagList()
        self.add_widget(f_taglist)
        f_taglist.addNewTag("kitty")
        f_taglist.addNewTag("cat")
        f_taglist.addNewTag("home")
        f_taglist.addNewTag("cute")
        f_taglist.addNewTag("kitty")

class TestApp(App):

    def build(self):
        return RootWidget()

if __name__ == '__main__':
    TestApp().run()