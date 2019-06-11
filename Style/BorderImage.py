from kivy.app import App
from kivy.lang import Builder

kv = '''
Widget:
    Button:
        pos: 200, 200
        canvas.before:
            BorderImage:
                source: 'tex.png'
                pos: self.x - 50, self.y - 50
                size: self.width + 100, self.height + 100
    Button:
        pos: 400, 400
        canvas.before:
            BorderImage:
                source: 'tex.png'
                pos: self.x - 15, self.y - 50
                size: self.width + 30, self.height + 100
    Button:
        pos: 500, 100
        canvas.before:
            BorderImage:
                source: 'tex.png'
                pos: self.x - 2, self.y - 2
                size: self.width + 4, self.height + 4
'''


class MyApp(App):
    def build(self):
        return Builder.load_string(kv)


MyApp().run()