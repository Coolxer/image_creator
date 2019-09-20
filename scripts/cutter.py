import bpy
import math
import random

class Cutter:
    def set(self, fth, angle):
        self.object = bpy.data.objects[str(fth)] # get cutter object

        self.width = self.object.dimensions[0] # cutter width dimension
        self.height = self.object.dimensions[2] # cutter height dimension
        self.radius = self.width / 2 # radius of cutter in millimetes

        self.object.select_set(True) # select cutter object as active

        self.angle = angle

        # randomize cutter rotation

        self.object.rotation_euler = (0, 0, 0)

        rot = random.randint(0, 359)

        self.object.rotation_euler = (0, 0, rot)

        # calcs to make properly angle

        y = (2 * math.pi * self.radius) / 360

        ka = (math.tan(math.radians(self.angle)) * self.height) / y

        screw_modifier = self.object.modifiers['Screw']
        screw_modifier.angle = math.radians(ka)
