import sys
import os
import cv2

class Imager:
    def __init__(self):
        self.directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'images'))
    def crop(self, img):
        height, width, _ = img.shape
        self.crop_width = int(self.crop_width)
        cx = int(width/2 - self.crop_width/2)
        cropped = img[0:height, cx:cx + self.crop_width]
        self.im.append(cropped)
        
    def read_and_operate(self):
        x = 0

        for x in range(self.image_count):
            img = cv2.imread(self.directory + '\img' + str(x) + '.png')
            self.crop(img)

    def concatenate_single(self):
        self.im_h = cv2.hconcat(self.im)

        try:
            x = 0
            for x in range(self.image_count):
                os.remove(self.directory + '\img' + str(x) + '.png')
        except: pass

    def cocatenate_multi(self):
        # check if the file already exists

        self.concatenate_single()

        file = None

        if os.path.isfile(self.output):
            file = cv2.imread(self.output)

            file = cv2.hconcat([file, self.im_h])
        else:
            file = cv2.hconcat([self.im_h])

        cv2.imwrite(self.output, file)


    def create(self, count, width, cutter_angle):
        self.im = []
        self.image_count = count 
        self.crop_width = width

        self.output = os.path.join(self.directory, str(cutter_angle) + '.png')

        self.read_and_operate()
        self.cocatenate_multi()

