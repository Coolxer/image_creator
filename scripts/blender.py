import bpy
import os
import calculator as calc

class Blender:
    def __init__(self):
        self.output_dir = os.path.dirname(bpy.data.filepath) + '\images' # the directory for storing images
        self.calculator = calc.Calculator()
        
    def generate(self, feathers, pictures_count, cutter_angle):
        self.calculator.calculate(feathers, pictures_count, cutter_angle)

        x = 0 # loop variable

        for x in range(pictures_count):
            path = os.path.join(self.output_dir , "img" + str(x) + ".png") # create unique img name
            self.calculator.scene.object.filepath = path # set path as render output path
            bpy.ops.render.render( write_still=True ) # save render img to file 
            bpy.ops.transform.rotate(value=self.calculator.angle, orient_axis='Z') # rotate object by angle 
            
        return self.calculator.steps_in_px
        #bpy.ops.transform.rotate(value=-angle * count, orient_axis='Z') # restore cutter rotation since operation started