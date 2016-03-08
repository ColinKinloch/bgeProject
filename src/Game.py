import bge
import Menu
from Controller import Hat

hat = Hat(0)

menu = Menu.Menu([
  Menu.Item('Continue'),
  Menu.Item('New Game'),
  Menu.Item('Settings'),
  Menu.Item('Quit')
])

def menuInit(co):
  global menu
  s = bge.logic.getCurrentScene()
  pos = 0
  p = s.objects['Menu']
  for item in menu:
    obj = s.addObject('MenuItem', p)
    obj.setParent(p)
    label = obj.groupMembers['Text']
    cursor = obj.groupMembers['Cursor']
    label.setParent(obj)
    cursor.setParent(obj)
    obj.position[2] += pos
    label.text = item.label
    item.display = cursor
    pos -= 1.25 * p.scaling[2]
    #obj.replaceMesh('Cube.001')

def menuStep(co):
  global hat, menu
  s = bge.logic.getCurrentScene()
  j = bge.logic.joysticks[0]
  h = j.hatValues[0]
  hat.update(h)
  
  if hat.justPressed(Hat.down.value):
    menu.next()
  if hat.justPressed(Hat.up.value) :
    menu.previous()
  for item in menu:
    if item is menu.current():
      item.display.playAction('Selected', 0, 25, play_mode=bge.logic.KX_ACTION_MODE_LOOP)
    else:
      item.display.playAction('Selected', 0, 0, play_mode=bge.logic.KX_ACTION_MODE_LOOP)

def controllerSetup(co):
  global hat, menu
  s = bge.logic.getCurrentScene()
  j = bge.logic.joysticks[0]
  h = j.hatValues[0]
  hat.update(h)
  
  if hat.justPressed(Hat.down.value):
    menu.next()
  if hat.justPressed(Hat.up.value) :
    menu.prev()

  s.objects["Menu"].text = menu.render()
