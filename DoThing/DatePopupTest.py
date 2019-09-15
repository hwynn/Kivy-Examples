from datetime import datetime
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, NumericProperty, ListProperty, ObjectProperty
import SimulateOutside

Builder.load_string('''
<DateEditButton>:
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
        popup_trigger = DateEditButton()
        self.top_label0 = ColorLabel(size_hint_y=None, height=50, text=str(datetime.strptime(popup_trigger.ISODateString, "%Y-%m-%dT%H:%M:%S")),
                                     bcolor=[.6, .3, .4, 1])
        self.top_label1 = ColorLabel(size_hint_y=None, height=50, text=str(popup_trigger.timeChunk1),
                                     bcolor=[.6, .3, .4, 1])
        self.top_label2 = ColorLabel(size_hint_y=None, height=50, text=str(popup_trigger.timeChunk2),
                                     bcolor=[.6, .3, .4, 1])
        # this detects changes in the series values and calls changes to the user interface be made
        popup_trigger.bind(ISODateString=self.update_date)
        self.add_widget(self.top_label0)
        self.add_widget(self.top_label1)
        self.add_widget(self.top_label2)
        self.add_widget(popup_trigger)

    def update_date(self, instance, value):
        # this function updates the installment number shown on the user interface whenever the value changes
        self.top_label0.text = str(datetime.strptime(value, "%Y-%m-%dT%H:%M:%S"))




class seriesFrame(BoxLayout):
    def __init__(self, **kwargs):
        super(seriesFrame, self).__init__(**kwargs)


class SimplePopup(Popup):
    def __init__(self, **kwargs):
        super(SimplePopup, self).__init__(**kwargs)
    # the widget we add in here actually does everything. so this is empty


def isNumberBlank(p_str):
    #decides if string is useable number
    #we will count '' as a number because we'll replace those with 0
    return ((p_str.isnumeric()) or (p_str==""))

def getNumberBlank(p_str):
    #gives us a useable number from a string
    #p_str must be tested by isNumberBlank() before being passed to this function
    if(p_str==""):
        return 0
    return int(p_str)


# this button is reuasable
class DateEditButton(Button):
    # this is the button that triggers the popup being created
    sampledate = datetime(1, 2, 3, 4, 5, 6)
    ISODateString = StringProperty(sampledate.isoformat())
    timeChunk1 = NumericProperty(sampledate.timetuple()[0])
    timeChunk2 = NumericProperty(sampledate.timetuple()[1])
    timeChunk3 = NumericProperty(sampledate.timetuple()[2])
    timeChunk4 = NumericProperty(sampledate.timetuple()[3])
    timeChunk5 = NumericProperty(sampledate.timetuple()[4])
    timeChunk6 = NumericProperty(sampledate.timetuple()[5])
    pops = SimplePopup()

    def __init__(self, **kwargs):
        super(DateEditButton, self).__init__(**kwargs)
        self.c_debug = 0
        self.text = "Fire Popup !"

    def setDateValue(self, p_ins):
        # this calls an outside script to set the series value in a picture file
        # then the new value is passed back to us for the user interface to display
        if self.c_debug > 0: print("DateEditButton.setDateValue:", p_ins)
        f_success = SimulateOutside.setOriginalDate(SimulateOutside.g_file, p_ins)
        if f_success:
            self.sampledate = SimulateOutside.getOriginalDate(SimulateOutside.g_file)
            self.ISODateString = self.sampledate.isoformat()
            self.timeChunk1 = self.sampledate.timetuple()[0]
            self.timeChunk2 = self.sampledate.timetuple()[1]
            self.timeChunk3 = self.sampledate.timetuple()[2]
            self.timeChunk4 = self.sampledate.timetuple()[3]
            self.timeChunk5 = self.sampledate.timetuple()[4]
            self.timeChunk6 = self.sampledate.timetuple()[5]
            if self.c_debug > 0: print("DateEditButton.setDateValue:", self.ISODateString)
        else:
            if self.c_debug > 0: print("setDateValue.setValue() operation not successful")

    def pop_cancel(self, instance):
        # any input from the user is discarded and the popup is closed
        if self.c_debug > 0: print("DateEditButton.pop_cancel.instance:", instance)
        self.pops.dismiss()

    def pop_submit(self, instance):
        # this happens when the submit button on the popup is pressed.
        # this checks input, tells the program the input is ready, then closes the popup
        f_timeInput1 = instance.parent.children[8]  # these are the text inputs with the values we will check
        f_timeInput2 = instance.parent.children[7]
        f_timeInput3 = instance.parent.children[6]
        f_timeInput4 = instance.parent.children[5]
        f_timeInput5 = instance.parent.children[4]
        f_timeInput6 = instance.parent.children[3]
        # if the input is invalid, the button shouldn't work.
        # This lets the user know a mistake happened before their work is lost when the popup closes
        if self.c_debug > 0: print("DateEditButton.pop_submit.children[8]:", f_timeInput1.text)
        if self.c_debug > 0: print("DateEditButton.pop_submit.children[7]:", f_timeInput2.text)
        if self.c_debug > 0: print("DateEditButton.pop_submit.children[6]:", f_timeInput3.text)
        if self.c_debug > 0: print("DateEditButton.pop_submit.children[5]:", f_timeInput4.text)
        if self.c_debug > 0: print("DateEditButton.pop_submit.children[4]:", f_timeInput5.text)
        if self.c_debug > 0: print("DateEditButton.pop_submit.children[3]:", f_timeInput6.text)
        if self.areDateStringsValid(f_timeInput1.text, f_timeInput2.text, f_timeInput3.text, f_timeInput4.text, f_timeInput5.text, f_timeInput6.text):
            f_datetime = datetime(getNumberBlank(f_timeInput1.text),
                                  getNumberBlank(f_timeInput2.text),
                                  getNumberBlank(f_timeInput3.text),
                                  getNumberBlank(f_timeInput4.text),
                                  getNumberBlank(f_timeInput5.text),
                                  getNumberBlank(f_timeInput6.text))
            self.setDateValue(f_datetime)
            self.pops.dismiss()
        # TODO: allow special case for 2 empty inputs, implying the user wants to remove series metadata
        # TODO: add feedback for bad inputs

    def areDateStringsValid(self, p_year, p_month, p_day, p_hour, p_minute, p_second):
        # before we accept this date time input, we have to check if it's valid
        # and we just have a bunch of strings at this point
        if p_year == "" or (p_year.isnumeric()==False):
            return False
        if (isNumberBlank(p_month) and isNumberBlank(p_day) and isNumberBlank(p_hour)
                and isNumberBlank(p_minute) and isNumberBlank(p_second))==False:
            return False
        try:
            #we'll try to create a datatime. its constructor will find any problems for us
            dt_obj = datetime(getNumberBlank(p_year), getNumberBlank(p_month), getNumberBlank(p_day),
                              getNumberBlank(p_hour), getNumberBlank(p_minute), getNumberBlank(p_second))
            return True
        except:
            # TODO: add exception saying that number isn't valid
            print('DateEditButton.areDateStringsValid(): not valid')
            return False

    def fire_popup(self):
        # this builds the interface inside the pupup, then makes it appear on the screen
        f_widget = BoxLayout(orientation='vertical')
        self.pops.content = f_widget

        insInput1 = TextInput(multiline=False, size_hint=(None,None), height=30, width=50,
                              input_filter='int', text=str(self.timeChunk1))
        insInput2 = TextInput(multiline=False, size_hint=(None,None), height=30, width=30,
                              input_filter='int', text=str(self.timeChunk2))
        insInput3 = TextInput(multiline=False, size_hint=(None,None), height=30, width=30,
                              input_filter='int', text=str(self.timeChunk3))
        insInput4 = TextInput(multiline=False, size_hint=(None,None), height=30, width=30,
                              input_filter='int', text=str(self.timeChunk4))
        insInput5 = TextInput(multiline=False, size_hint=(None,None), height=30, width=30,
                              input_filter='int', text=str(self.timeChunk5))
        insInput6 = TextInput(multiline=False, size_hint=(None,None), height=30, width=30,
                              input_filter='int', text=str(self.timeChunk6))
        insLabel = Label(text=str(self.timeChunk1))

        f_widget.add_widget(insInput1)
        f_widget.add_widget(insInput2)
        f_widget.add_widget(insInput3)
        f_widget.add_widget(insInput4)
        f_widget.add_widget(insInput5)
        f_widget.add_widget(insInput6)
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