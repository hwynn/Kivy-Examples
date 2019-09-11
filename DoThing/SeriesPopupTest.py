from kivy.app import App
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ListProperty

Builder.load_string('''
<SimpleButton>:
    on_press: self.fire_popup()
<SimplePopup>:
    id:pop
    size_hint: .4, .6
    pos_hint: {'x': .6, 'y': .2}
    pos: 200, 0
    auto_dismiss: False
    title: 'Hello world!!'
    
    #Button:
    #    text: 'Click here to dismiss'
    #    on_press: pop.dismiss()
    
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
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        top_label1 = ColorLabel(size_hint_y=None, height=50, text='The silly frog', bcolor=[.3, .7, .5, 1])
        top_label2 = ColorLabel(size_hint_y=None, height=50, text=str(5), bcolor=[.6, .3, .4, 1])
        self.add_widget(top_label1)
        self.add_widget(top_label2)
        self.add_widget(SimpleButton())

class seriesFrame(BoxLayout):
    def __init__(self, **kwargs):
        super(seriesFrame, self).__init__(**kwargs)

class SimplePopup(Popup):
    def __init__(self, **kwargs):
        super(SimplePopup, self).__init__(**kwargs)
    #the widget we add in here actually does everything. so this is empty

class SimpleButton(Button):
    #this is the button that triggers the popup being created
    seriesIns = NumericProperty(-1)
    seriesName = StringProperty("")
    tempSeriesIns = seriesIns
    tempSeriesName = seriesName
    insReady = False
    nameReady = False
    submit = BooleanProperty(False)
    edit = BooleanProperty(False)


    def __init__(self, **kwargs):
        super(SimpleButton, self).__init__(**kwargs)

    def on_edit(self, instance, value):
        if instance.submit:
            pass
        pass

    text = "Fire Popup !"
    c_seriesName = StringProperty("Frog's big day")
    c_seriesInstallment = NumericProperty(4)
    pops = SimplePopup()

    def pop_cancel(self, instance):
        self.pops.dismiss()

    def fire_popup(self):
        f_widget = BoxLayout(orientation='vertical')
        self.pops.content = f_widget
        f_input1 = TextInput()
        f_input2 = TextInput()
        f_label1 = Label(text='test label')
        f_label2 = Label(text='7')
        f_widget.add_widget(f_label1)
        f_widget.add_widget(f_label2)
        f_button1 = Button(text='submit button', on_press=self.pop_cancel)
        self.bind(c_seriesName=f_label1.setter('text'), c_seriesInstallment=f_label2.setter('text'))
        Clock.schedule_once(lambda dt: self.property('c_seriesName').dispatch(self), 0.2)
        f_widget.add_widget(f_button1)
        self.pops.open()




class SampleApp(App):
    def build(self):
        return RootWidget()

SampleApp().run()