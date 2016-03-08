from bpy import data, ops, context
import os
import json

# Reset Scene
'''override = context.copy()
override['selected_bases'] = list(context.scene.object_bases)
ops.object.delete(override)'''

scene = data.scenes['Scene']
scene.name = 'Old'
scene.camera = None
data.scenes.new('Scene')
data.scenes.remove(scene)
scene = data.scenes['Scene']

for camera in data.cameras:
  data.cameras.remove(camera)

# Set Scene
scene.render.engine = 'BLENDER_GAME'
gs = scene.game_settings
gs.material_mode = 'GLSL'

# Import scripts to text
srcDir = './src'
for f in os.listdir(srcDir):
  ops.text.open(filepath = (srcDir + '/' + f), internal = True)

# Import scenes
