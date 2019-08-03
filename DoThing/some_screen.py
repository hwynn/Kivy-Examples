#!/usr/bin/env python

from kivy.app import App
from kivy.uix.screenmanager import Screen

from lib.modules.adaptive_grid_layout import Adaptive_GridLayout


class Some_Screen(Screen):
  def __init__(self, **kwargs):
    super(Some_Screen, self).__init__(**kwargs)

  def attach_adaptive_grid(self, grid_id, parent, clear = False):
    if clear:
      parent.clear_widgets(children = parent.children)

    new_grid = Adaptive_GridLayout(cols = 1, id = grid_id, grow_rows = True)
    return parent.add_widget(new_grid)


class ScreenApp(App):
    def build(self):
        return Some_Screen()

if __name__ == '__main__':
    ScreenApp().run()
