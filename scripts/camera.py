import bpy

class Camera:
    def __init__(self, scene):
        self.object = bpy.data.objects['Camera']
        self.width = scene.resolution_x # resolution width of camera render in blender
        self.height = scene.resolution_y # resolution height of camera render in blender
        #self.ortho_scale = self.object.ortho_scale # camera zoom parameter
        