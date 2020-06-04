import numpy
import numpy as np
from matplotlib import pyplot as pp
import matplotlib.image as img
import os
import sys
from PIL import Image
import math


###########################################################################################
# Importing the Images(21) from the directory
###########################################################################################
for infile in os.listdir('.'):
    if infile.endswith('.png'):
        matrix = img.imread(infile)
        m = Image.open(infile)
        fn, ftext = os.path.splitext(infile)
        m1 = m.size[0]  # width of the image (x-axis)
        m2 = m.size[1]  # height of the image (y-axis)
        print(m2/3)
        print ("Image Size:", m.size)

        #####################################################################
        # Finding non-zero pixel value to get the co-ordinate values (Centre)
        #####################################################################
        a = []
        for j in range(0, int(m2 / 3)):
            for i in range(int(m1 / 3), int(3 * m1 / 4)):
                if sum(m.getpixel((i, j))) >= 255:
                    a.append((i, j))
                    break
        a = a[0]
        [C1, C4] = a
        ####################################################################
        # Finding non-zero pixel value to get the co-ordinate values (Left)
        ####################################################################

        b = []
        for i in range(0, m1 / 4):
            for j in range(m2 / 2, 4 * m2 / 5):
                if sum(m.getpixel((i, j))) >= 30:
                    b.append((i, j))
                    break
        b = b[0]
        [C2, C5] = b

        #####################################################################
        # Finding non-zero pixel value to get the co-ordinate values (Left)
        #####################################################################
        c = []
        for i in range(12 * m1 / 13, m1/3, -1):
            for j in range(12 * m2 / 13, m2 / 3, -1):
                if sum(m.getpixel((i, j))) >= 30:
                    c.append((i, j))
                    break
        c = c[0]
        [C3, C6] = c
        print ("Detected Co-ordinates values :",'centre',(C1,C4),'Left', (C2,C5),'Right', (C3,C6))

        #####################################################################
        # Best Model Matching Selection
        #####################################################################
        Pixel_values = 0
        for i in range(-4, 5):
            for j in range(-4, 5):
                Cx = C1 + i/4
                Cx1 = C2 + i
                Cx2 = C3 + i
                Cy = C4 + j
                Cy1 = C5 + j
                Cy2 = C6 + j

                ########################################################################
                # Radius & Angle Calculation
                #######################################################################
                from Task22 import Angle_Radius

                Radius, Angle11, Angle22 = Angle_Radius(Cx, Cy, Cx1, Cy1, Cx2, Cy2)

                ########################################################################
                # Mask Creation [563,0,22,532,1106,537]
                #######################################################################
                from Task33 import Pie_mask

                centre = (Cx, Cy)
                Angle = (Angle11, Angle22)
                mask = Pie_mask(matrix.shape, (Cy, Cx), Radius, (-Angle11, -Angle22))
                a1 = matrix[mask]
                a1 = np.sum(a1)
                if a1 > Pixel_values:
                    Pixel_values = a1
                    best_Cx = Cx
                    best_Cy = Cy
                    best_Cx1 = Cx1
                    best_Cx2 = Cx2
                    best_Cy1 = Cy1
                    best_Cy2 = Cy2
                    #print "The best pixel value is :", Pixel_values, "The best Cordinate values :", [Cx, Cy, Cx1, Cy1, Cx2, Cy2]
        print ("Best pixel value:", Pixel_values)
        print ("Best Cordinate values:", [best_Cx, best_Cy, best_Cx1, best_Cy1,best_Cx2, best_Cy2])

        ######################################################################################################################################
        #   Image Cropping with best Modal Matching values
        ######################################################################################################################################
        Radius, Angle11, Angle22 = Angle_Radius(best_Cx, best_Cy, best_Cx1, best_Cy1, best_Cx2, best_Cy2)
        print ("Radius:", Radius, "Starting angle", Angle11, "Ending angle", Angle22)
        centre = (best_Cx, best_Cy)
        Angle = (Angle11, Angle22)
        mask = Pie_mask(matrix.shape, (best_Cy, best_Cx), Radius, (-Angle11, -Angle22))
        matrix[~mask] = (100, 10, 100)
        pp.imshow(matrix)
        #pp.show()
        pp.savefig('100/{}{}'.format(fn, ftext))