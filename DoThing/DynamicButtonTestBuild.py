from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, DictProperty
from kivy.factory import Factory
#https://stackoverflow.com/questions/2349991/how-to-import-other-python-files
from DynamicButtonList import DynamicTagList

"""
This is an example of using our custom class to dynamically create and close buttons
"""


Builder.load_string('''
<DynamicTagList>:
	spacing: 5, 5
''')

class TestApp(App):

    def build(self):
        return DynamicTagList()

    def on_stop(self):
        print("TestApp.on_stop: finishing")
        a_frame = self.root.getTarget('DynamicTag')[0]
        #a_frame.debugSize()
        print(self.root.getTagList())

if __name__ == '__main__':
    TestApp().run()