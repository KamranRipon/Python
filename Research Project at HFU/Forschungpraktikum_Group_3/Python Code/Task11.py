import numpy
import numpy as np
import math
import matplotlib.image as img
from matplotlib import pyplot
import os
####################################################################
# Getting the Co-ordinate values
####################################################################
Files = ['pat00008_1-1-1-1-2-10-1.mp4.cover.png']
matrix = img.imread(input('enter the image name'))
#   matrix = img.imread(Files[0])
pyplot.imshow(matrix)
pyplot.show()

#####################################################################
# Assigning the Co-ordinate values
#####################################################################
[C1, C4, C2, C5, C3, C6] = input('Enter the co-ordinates values')

#####################################################################
# Best Model Matching Selection
#####################################################################
a = 0
for i in range(-4, 5):
    for j in range(-4, 5):
        Cx = C1
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
        #   a1 = np.dot(mask, matrix)   # multiplying mask with the image pixels
        #   a1 = a1.sum()   # summing all the image pixel values (pixel values under mask)
        a1 = np.sum(a1)
        print 'a1 values are', a1
        if a1 > a:
            a = a1
            best_Cx = Cx
            best_Cy = Cy
            best_Cx1 = Cx1
            best_Cx2 = Cx2
            best_Cy1 = Cy2
            best_Cy2 = Cy2
            print "The best pixel value is :", a, "The best Cordinate values :", [Cx, Cy, Cx1, Cy1, Cx2, Cy2]
print "The best pixel value is :", a, "The best Cordinate values :", [best_Cx, best_Cy, best_Cx1, best_Cy1, best_Cx2,best_Cy2]

######################################################################################################################################
#   Image Cropping with best Modal Matching values [340, 12, 79, 296, 579, 296] [340, 4, 79, 286, 579, 288
######################################################################################################################################
Radius, Angle11, Angle22 = Angle_Radius(best_Cx, best_Cy, best_Cx1, best_Cy1, best_Cx2, best_Cy2)
print "Radius:", Radius, "Starting angle", Angle11, "Ending angle", Angle22
centre = (best_Cx, best_Cy)
Angle = (Angle11, Angle22)
mask = Pie_mask(matrix.shape, (best_Cy, best_Cx), Radius, (-Angle11, -Angle22))
matrix[~mask] = (100, 10, 100)
fn,fext = os.path.splitext(matrix)
pyplot.savefig('100/{}{}'.format(fn, fext))
pyplot.imshow(matrix)
pyplot.show()
