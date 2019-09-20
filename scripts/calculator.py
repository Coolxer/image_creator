import math
import scene

class Calculator:
    def __init__(self):
        self.scene = scene.Scene()

    def calculate(self, feathers, pictures_count, cutter_angle):

        self.scene.set(feathers, cutter_angle)

        self.pictures_count = pictures_count

        self.angle = math.radians(360) / self.pictures_count

        self.step_in_mm = math.sqrt((2*(self.scene.cutter.radius**2))*(-math.cos(self.angle) + 1))

        self.steps_in_px = (self.scene.camera.height * self.step_in_mm) / self.scene.cutter.height

        '''
        step_in_mm = 0.5 # width of single image in millimetes
        self.steps_in_px = (self.scene.camera.height * step_in_mm) / self.scene.cutter.height

        cos = (step_in_mm**2 - (2*(self.scene.cutter.radius**2))) / (-2*(self.scene.cutter.radius**2)) # cosinus value from cosine theorem ("twierdzenie cosinusow")
                                                        # step_in_mm^2 = r^2 + r^2 - 2*r*r*cosa

        self.angle = math.acos(cos) # angle in radians calculated by cos value

        self.count = int(round((math.radians(360)) / self.angle)) # number of parts to created depend on angle
        '''