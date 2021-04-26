# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:29:50 2020

@author: kel
"""
#This script shows how to import a dataset into Python that is downloaded from KONECT.

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

##################### START: Example network graphing #######################

# next few lines plot the layout of the network
#plt.figure(101, figsize=(10, 10))
#plt.axes([0,0,0.7,0.6])
#plt.title('Directed Network: Florida Ecosystem, Wet')
#pos = nx.spring_layout(dg) # spring_layout is an layout of the vertices.
#nx.draw_networkx_nodes(dg, pos, node_size = 25) # this plots nodes
#nx.draw_networkx_edges(dg, pos, width = .5) # this plot edges

##################### END: Example graphing from previous project #######################

##################### START: Example Histogram #####################

# plt.figure(102, figsize=(10, 10))
# plt.axes([0,0,0.7,0.6])
# plt.title('Histogram of the vertex degrees in the Florida Ecosystem Wet graph. Mean = '+'{0:.2f}'.format(mn)+ '; STD = '+'{0:.2f}'.format(sd))
# plt.hist(vec_deg, bins = 10) 

##################### END: Example Histogram #######################

##################### START: Part A #####################

# Set up graph domain
# Graph starts at x=1, goes to x=10, in steps of 1
t = np.arange(1, 10, 0.01)

a1 = 0.5*t
a2 = t - (t//2) + 1

figA, axA = plt.subplots()
axA.plot(t, a1)
axA.plot(t, a2)

axA.set(xlabel="TODO: Description", ylabel="TODO: Description", title="TODO: PartA title")

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

axB.set(xlabel="TODO: Description", ylabel="TODO: Description", title="TODO: PartB title")

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

axC.set(xlabel="", ylabel="", title="TODO: PartC title")

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

axD.set(xlabel="", ylabel="", title="TODO: PartD title")

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

axE.set(xlabel="", ylabel="", title="TODO: PartE title")

axE.grid()

plt.show()

##################### END: Part D #######################