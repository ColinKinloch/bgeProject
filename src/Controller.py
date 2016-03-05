from enum import Enum

class Hat(Enum):
  none = 0
  up = 1
  right = 2
  down = 4
  left = 8
  def __init__(self, value):
    self.current = value
    self.previous = 0
  def update(self, value):
    self.previous = self.current
    self.current = value
  def pressed(self, value):
    return bool(self.current & value)
  def justPressed(self, value):
    return self.pressed(value) and bool((self.previous ^ self.current) & value)
