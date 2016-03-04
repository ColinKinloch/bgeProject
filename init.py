import bpy
import os

# Import scripts to text
srcDir = './src'
for f in os.listdir(srcDir):
  bpy.ops.text.open(filepath = (srcDir + '/' + f), internal = True)
