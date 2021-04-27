# -*- coding: utf-8 -*-
"""
Created on Mon April 27 2021

@author: Aidan Becker and Abrar Ahmad
"""

import matplotlib.pyplot as plt
import numpy as np
import math

################### START: Basic Setup ######################

# I believe this is only necessary if the program is run multiple times in succession
# Almost no performance impact, can't really hurt though
# Might as well leave it in
plt.close('all')

# Raise font size to match higher quality images
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

plt.rc('font', **font)

# PLEASE READ
# These images are probably VERY low resolution to start.
# To get higher quality images, you can go to Tools->Preferences->IPython console->Graphics
# Under Inline backend, at least raise the width & height to ~10 each.
# I'm currently using 15, 15, with a dpi of 100. 
# You will probably need to restart Spyder for these changes to take effect.

################### END: Basic Setup ######################

##################### START: Part A #####################

# Set up graph domain
# Graph starts at x=1, goes to x=10, in steps of 1
t = np.arange(1, 10, 0.01)

a1 = 0.5*t
a2 = t - (t//2) + 1

figA, axA = plt.subplots()
axA.plot(t, a1)
axA.plot(t, a2)

axA.set(xlabel="Blue: y = 0.5n, Orange: y = n − ⌊n^2⌋ + 1", ylabel="", title="n − ⌊n^2⌋ + 1 is Ω(0.5n) for all n ≥ 1")

axA.grid()

plt.show()

##################### END: Part A #######################

##################### START: Part B #####################

# Set up graph domain
# Graph starts at x=1, goes to x=10, in steps of 1
t = np.arange(3, 10, 0.01)

b1 = 0*t
b2 = t - (t//2) + 1
b3 = t

figB, axB = plt.subplots()
axB.plot(t, b1)
axB.plot(t, b2)
axB.plot(t, b3)

axB.set(xlabel="Blue: y = 0, Orange: y = n − ⌊n^2⌋ + 1, Green: y = n", ylabel="", title="n − ⌊n^2⌋ + 1 is O(n) for every n ≥ 3")

axB.grid()

plt.show()

##################### END: Part B #######################

##################### START: Part C #####################

# Set up graph domain
# Graph starts at x=1, goes to x=10, in steps of 1
t = np.arange(3, 10, 0.01)

c1 = t*t
c2 = 3*t*(t-2)
c3 = 4*(t*t)

figC, axC = plt.subplots()
axC.plot(t, c1)
axC.plot(t, c2)
axC.plot(t, c3)

axC.set(xlabel="Blue: y = n^2, Orange: y = 3n(n-2), Green: y = 4(n^2)", ylabel="", title="3n(n-2) is Θ(n^2) for every n ≥ 3")

axC.grid()

plt.show()

##################### END: Part C #######################

##################### START: Part D #####################

# Set up graph domain
# Graph starts at x=1, goes to x=10, in steps of 1
t = np.arange(3, 10, 0.01)

d1 = 0.5*(t*t)
d2 = (t*(3*t - 2))/2

figD, axD = plt.subplots()
axD.plot(t, d1)
axD.plot(t, d2)

axD.set(xlabel="Blue: y = 0.5n^2, Orange: y = n(3n-2)/2", ylabel="", title="n(3n-2)/2 is Ω 0.5n^2 for every n ≥ 3")

axD.grid()

plt.show()

##################### END: Part D #######################

##################### START: Part E #####################

# Set up graph domain
# Graph starts at x=1, goes to x=10, in steps of 1
t = np.arange(2, 10, 0.01)

e1 = (t*t*t)*(1/6)
# I understand that there are issues with the following approximation of a ceiling() function
# But the libraries don't really want to work here. As long as the function is not equal to 0
# at any of the ranges we're looking at, ceiling(x) == floor(x) + 1
# So here, we just use integer division and add 1
e2 = (t*t)*((t//2 + 1) - 1)   
e3 = (t*t*t)

figE, axE = plt.subplots()
axE.plot(t, e1)
axE.plot(t, e2)
axE.plot(t, e3)

axE.set(xlabel="Blue: y = (n^3)/6, Orange: y = n^2(⌈n3⌉−1), Green: y = n^3", ylabel="", title="n^2(⌈n3⌉−1) is Θ(n^3) for every n ≥ 2")

axE.grid()

plt.show()

##################### END: Part D #######################