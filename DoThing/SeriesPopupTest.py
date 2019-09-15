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
        popup_trigger = SimpleButton()
        self.top_label1 = ColorLabel(size_hint_y=None, height=50, text=popup_trigger.seriesName, bcolor=[.3, .7, .5, 1])
        self.top_label2 = ColorLabel(size_hint_y=None, height=50, text=str(popup_trigger.seriesIns),
                                     bcolor=[.6, .3, .4, 1])
        # this detects changes in the series values and calls changes to the user interface be made
        popup_trigger.bind(seriesName=self.top_label1.setter('text'))
        popup_trigger.bind(seriesIns=self.update_installment)
        self.add_widget(self.top_label1)
        self.add_widget(self.top_label2)
        self.add_widget(popup_trigger)

    def update_installment(self, instance, value):
        # this function updates the installment number shown on the user interface whenever the value changes
        self.top_label2.text = str(value)


class seriesFrame(BoxLayout):
    def __init__(self, **kwargs):
        super(seriesFrame, self).__init__(**kwargs)


class SimplePopup(Popup):
    def __init__(self, **kwargs):
        super(SimplePopup, self).__init__(**kwargs)
    # the widget we add in here actually does everything. so this is empty


# this button is reuasable
class SimpleButton(Button):
    # this is the button that triggers the popup being created

    # these are the two values that make up the series information
    seriesIns = NumericProperty(4)
    seriesName = StringProperty("Frog's big day")
    pops = SimplePopup()

    def __init__(self, **kwargs):
        super(SimpleButton, self).__init__(**kwargs)
        self.c_debug = 0
        self.text = "Fire Popup !"

    def setSeriesValue(self, p_name, p_ins):
        # this calls an outside script to set the series value in a picture file
        # then the new value is passed back to us for the user interface to display
        if self.c_debug > 0: print("SimpleButton.setSeriesValue:", p_name, p_ins)
        f_success = SimulateOutside.setSeries(SimulateOutside.g_file, p_name, p_ins)
        if f_success:
            self.seriesName, self.seriesIns = SimulateOutside.getSeries(SimulateOutside.g_file)
        else:
            if self.c_debug > 0: print("setSeriesValue.setValue() operation not successful")

    def pop_cancel(self, instance):
        # any input from the user is discarded and the popup is closed
        if self.c_debug > 0: print("SimpleButton.pop_cancel.instance:", instance)
        self.pops.dismiss()

    def pop_submit(self, instance):
        # this happens when the submit button on the popup is pressed.
        # this checks input, tells the program the input is ready, then closes the popup
        f_nameInput = instance.parent.children[5]  # I think this would be a pointer in c++
        f_insInput = instance.parent.children[4]  # these are the text inputs with the values we will check
        # if the input is invalid, the button shouldn't work.
        # This lets the user know a mistake happened before their work is lost when the popup closes
        if self.isNameValid(f_nameInput.text) and self.isInstallmentValid(f_insInput.text):
            f_name = f_nameInput.text
            f_installment = int(f_insInput.text)
            self.setSeriesValue(f_name, f_installment)
            self.pops.dismiss()
        # TODO: allow special case for 2 empty inputs, implying the user wants to remove series metadata
        # TODO: add feedback for bad inputs

    def isNameValid(self, p_name):
        # before we accept this name, we have to check if it's valid
        if p_name != "" and len(p_name) < 100:  # arbitrary name size limit
            return True
        return False

    def isInstallmentValid(self, p_ins):
        # before we accept this installment, we have to check if it's valid
        if p_ins == "":
            return False
        if p_ins.isnumeric():
            if int(p_ins) > (0):
                return True
            # TODO: add exception saying that number isn't valid
        return False

    def fire_popup(self):
        # this builds the interface inside the pupup, then makes it appear on the screen
        f_widget = BoxLayout(orientation='vertical')
        self.pops.content = f_widget

        nameInput = TextInput(multiline=False, size_hint_y=None, height=30, text=self.seriesName)
        insInput = TextInput(multiline=False, size_hint_y=None, height=30, input_filter='int', text=str(self.seriesIns))

        nameLabel = Label(text=self.seriesName)
        insLabel = Label(text=str(self.seriesIns))

        f_widget.add_widget(nameInput)
        f_widget.add_widget(insInput)
        f_widget.add_widget(nameLabel)
        f_widget.add_widget(insLabel)
        f_button1 = Button(text='submit button', on_press=self.pop_submit)
        f_button2 = Button(text='cancel button', on_press=self.pop_cancel)
        f_widget.add_widget(f_button1)
        f_widget.add_widget(f_button2)
        self.pops.open()


class SampleApp(App):
    def build(self):
        return RootWidget()


SampleApp().run()