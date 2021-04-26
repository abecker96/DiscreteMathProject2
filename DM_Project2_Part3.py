# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:29:50 2020

@author: kel
"""
print('#####################################################################')
print('####### Directed weighted network: Florida Ecosystem wet ############')
print('#####################################################################') 
#This script shows how to import a dataset into Python that is downloaded from KONECT.

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

################### START: Clearing charts from memory ######################

# I believe this is only necessary if the program is run multiple times in succession
# Almost no performance impact, can't really hurt though
# Might as well leave it in
plt.close('all')

################### END: Clearing charts from memory ######################

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