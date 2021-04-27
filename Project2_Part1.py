########################################
#This is my contribution to the project#
########################################
"""
Created on Sat Apr 24 19:31:12 2021

@author: Abrar Ahmad
"""

import matplotlib.pyplot as plt
import numpy as num
import math as mt

plt.close('all')

#Experimenting with the linearly spaced numbers
x = num.linspace(-20,20,60)

#This is for part 1a
y1 = x/2
#y2 = mt.floor(y1) + 1 commented due to TypeError

####################
#This is for setting the axes at the center
#Code from scriptverse.academy
####################
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.title('Graph 1A')
plt.plot(x, y1, 'r')
#plt.plot(x, y2, 'b') 

plt.show()
plt.close() #This is for closing the plot after showing it

#I skipped to part 1c
y5 = x**2
y6 = 3*x*(x-2)
y7 = 4*(x**2)

plt.plot(x, y5, 'r', label = 'y=x^2')
plt.plot(x, y6, 'g', label = 'y=3x(x-2)')
plt.plot(x, y7, 'b', label = 'y=4x^2')

plt.legend(loc='upper center')

plt.show()
plt.close()

#I skipped to part 1d
y8 = y5/2
y9 = (x*(3*x-2))/2

plt.plot(x, y8, 'r', label = 'y=(x^2)/2')
plt.plot(x, y9, 'b', label = 'y=(x(3x-2))/2')
