import bge

class Item():
  def __init__(self, label):
    self.label = label

class Menu():
  #Submenu, menu as item, menu name, functors?
  def __init__(self, items):
    self.items = items
    self.i = 0
    self.cursor = '-'
  def __iter__(self):
    return iter(self.items)
  def next(self):
    self.i += 1
    if self.i >= len(self.items):
      self.i = 0
    return self.current()
  def previous(self):
    self.i -= 1
    if self.i < 0:
      self.i = len(self.items) - 1
    return self.current()
  def current(self):
    return self.items[self.i]
  def render(self):
    out = ''
    for i, item in enumerate(self.items):
      if i is self.i:
        out += self.cursor
      else:
        out += ' '
      out += item.label
      out += '\n'
    return out
