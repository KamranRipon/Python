import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5)
y = x ** 2

#plt.plot(x,y,'r-')

'''    Object Oriented Way   '''
      
###########################################
'''
#fig = plt.figure()

#axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
#axes2 = fig.add_axes([0.2,0.50,0.4,0.3])
#
#axes1.plot(x,y)
#axes2.plot(y,x)
#axes1.set_xlabel('X')
#axes1.set_ylabel('Y')
#
#axes2.set_xlabel('Y')
#axes2.set_ylabel('X')
'''
###########################################

''' A different Approach '''

fig,axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot(x,y)
axes[0].set_title('First Plot')

axes[1].plot(y,x)
axes[1].set_title('First Plot')

plt.tight_layout()

##########################################

''' Figure Size and DPI '''
