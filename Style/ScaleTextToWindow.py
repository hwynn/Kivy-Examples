from kivy.base import runTouchApp
from kivy.lang import Builder

runTouchApp(Builder.load_string('''
<ScaleLabel@Label>:
    text_size: self.width, None
    _scale: 1. if self.texture_size[1] < self.height else float(self.height) / self.texture_size[1]
    canvas.before:
        PushMatrix
        Scale:
            origin: self.center
            x: self._scale or 1.
            y: self._scale or 1.
    canvas.after:
        PopMatrix

ScaleLabel:
    text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
'''))