"""Render the loaded scene to PNG without saving changes to the .blend file."""
import argparse
import sys
from pathlib import Path

import bpy

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', required=True, help='Path for the rendered PNG.')
parser.add_argument('--frame', type=int, help='Optional frame; default is the saved frame.')
args = parser.parse_args(sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else [])
output = Path(args.output).expanduser().resolve()
if output.exists():
    raise FileExistsError('Choose a new output path: ' + str(output))
output.parent.mkdir(parents=True, exist_ok=True)
scene = bpy.context.scene
if args.frame is not None:
    scene.frame_set(args.frame)
scene.render.image_settings.file_format = 'PNG'
scene.render.image_settings.color_mode = 'RGBA'
bpy.ops.render.render()
bpy.data.images['Render Result'].save_render(str(output), scene=scene)
print('Rendered: ' + str(output))
