import os
from PIL import Image
import matplotlib.image as img


for infile in os.listdir('.'):
    if infile.endswith('.png'):
        matrix = img.imread(infile)
        m = Image.open(infile)
        fn, ftext = os.path.splitext(infile)
        m1 = m.size[0]  # width of the image (x-axis)
        m2 = m.size[1]  # height of the image (y-axis)
        print(m2)
        print ("Image Size:", m.size)
        
        
        #a = []
        #for j in range(0, m2 / 3):
#            for i in range(m1 / 3, 3 * m1 / 4):
#                if sum(m.getpixel((i, j))) >= 255:
#                    a.append((i, j))
#                    