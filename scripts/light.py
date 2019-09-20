import bpy

class Light:
    def __init__(self, name):
        self.object = bpy.data.lights[str(name)]

    def set_power(self, value):
        self.object.energy = value
        