import bpy
import camera as cam
import cutter as ctt
import light as lt
import random

class Scene:
    def __init__(self):
        self.object = bpy.data.scenes['Scene'].render
        self.camera = cam.Camera(self.object)
        self.cutter = ctt.Cutter()

        self.light1 = lt.Light('area_light_1')
        self.light2 = lt.Light('area_light_2')

    def set(self, feathers, cutter_angle):
        colls = bpy.data.collections

        for c in colls:
            c.hide_render = True

        bpy.data.collections[str(feathers)].hide_render = False

        self.cutter.set(feathers, cutter_angle)

        random_power = random.randint(200, 1500)
        print(random_power)
        self.light1.set_power(random_power)
        self.light2.set_power(random_power)