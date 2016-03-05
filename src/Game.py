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
  scale = 0.2
  for item in menu:
    print(item.label)
    #obj = bge.types.KX_GameObject(s)
    obj = s.addObject('Empty', 'MenuLoc')
    obj.position[2] += pos
    obj.scaling = [scale, scale, scale]
    obj.children['Text'].text = item.label
    item.display = obj.children['Cursor']
    pos -= 1.25 * scale
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
