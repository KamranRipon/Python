import numpy
import numpy as np
import math
import matplotlib.image as img
from matplotlib import pyplot as pp


############################################################################################################################################
#   Mask Function
############################################################################################################################################s
def Pie_mask(shape, centre, Radius, Angle):
    x, y = np.ogrid[:shape[0], :shape[1]]
    cx, cy = centre
    Anglemin, Anglemax = np.deg2rad(Angle)

    if Anglemax < Anglemin:
        Anglemax += 2 * np.pi

    r2 = (x - cx) * (x - cx) + (y - cy) * (y - cy)
    theta = np.arctan2(x - cx, y - cy) - Anglemin
    theta %= (2 * np.pi)
    cirmask = r2 <= Radius * Radius
    anglemask = theta <= (Anglemax - Anglemin)
    return cirmask * anglemask
