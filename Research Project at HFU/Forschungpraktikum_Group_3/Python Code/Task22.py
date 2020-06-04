import numpy
import numpy as np
import math
import matplotlib.image as img
from matplotlib import pyplot as pp

############################################################################################################################################
#   Defining the function for Angle and Radius Calculation
############################################################################################################################################

def Angle_Radius(Cx, Cy, Cx1, Cy1, Cx2, Cy2):

    ######################################################################
    #   Setting Desired co-ordinates as origin
    ######################################################################
    Cx1_mod = Cx - Cx1
    Cy1_mod = Cy - Cy1
    Cx2_mod = Cx - Cx2
    Cy2_mod = Cy - Cy2

    ######################################################################
    #   ANGLE Calculation
    ######################################################################
    Angle1 = math.atan2(Cy1_mod - 0, Cx1_mod - 0)
    Angle2 = math.atan2(Cy2_mod - 0, Cx2_mod - 0)
    Angle = abs(Angle2) - abs(Angle1)
    Angle11 = math.degrees(Angle1)
    Angle22 = math.degrees(Angle2)

    ######################################################################
    #   Radius Calculation
    ######################################################################
    Radius1 = ((Cx - Cx1) ** 2 + (Cy - Cy1) ** 2)
    Radius1 = math.sqrt(Radius1)
    Radius2 = ((Cx - Cx2) ** 2 + (Cy - Cy2) ** 2)
    Radius2 = math.sqrt(Radius2)
    if Radius1 > Radius2:
        Radius = Radius1
    else:
        Radius = Radius2
    return Radius, Angle11, Angle22
