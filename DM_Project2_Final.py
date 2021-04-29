# -*- coding: utf-8 -*-
"""
Created on Mon April 27 2021

@author: Aidan Becker and Abrar Ahmad
"""

import matplotlib.pyplot as plt
import numpy as np
from timeit import default_timer as timer
import time

################### START: Basic Setup ######################
#Leave this block uncommented all the time

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


# Python program for implementation of MergeSort
# from: https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr):
    if len(arr) > 1: 
        # Divide the array in 2 halves
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        
        # Sorting both halves
        mergeSort(L)
        mergeSort(R)
        
        # 'zip' both sorted halves into a final array
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was missed
        # If it was, add it to the main array
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        # Check the other half
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            
def mergeSortEstimate(n):
    if n <= 1:
        return 0
    else:
        return mergeSortEstimate(np.floor(n/2)) + mergeSortEstimate(np.ceil(n/2)) + (n-1)
            
# Define insertionSort algorithm
def insertionSort(arr):
    # Algorithm listed in textbook:
    # x = a[k]
    # j = k-1
    # while(j != 0)
    #   if(x<a[j])
    #       a[j+1] = a[j]
    #       a[j] = x
    #       j = j-1
    # next k
    
    # loop through every element of the array
    for k in range(1, len(arr)):
        # set x to be the element we're looking at (key element)
        x = arr[k]
        # set j to be the index of the element before this one in the array (inspection element)
        j = k-1
        # while there still is an element before the one we're looking at
        while(j >= 0):
            # if the inspection element before the key element is larger
            if(x < arr[j]):
                # swap the positions of the key and inspection elements
                arr[j+1] = arr[j]
                arr[j] = x
            # decrement index of inspection element
            j = j-1
   
# Define a helper function to reverse an array
def Reverse(lst):
    return [ele for ele in reversed(lst)]

################### END: Basic Setup ######################



##################### START: Section 1 #####################

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

axB.set(xlabel="Blue: y = 0, Orange: y = n − ⌊n/2⌋ + 1, Green: y = n", ylabel="", title="n − ⌊n/2⌋ + 1 is O(n) for every n ≥ 3")

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

axE.set(xlabel="Blue: y = (n^3)/6, Orange: y = n^2(⌈n/3⌉−1), Green: y = n^3", ylabel="", title="n^2(⌈n/3⌉−1) is Θ(n^3) for every n ≥ 2")

axE.grid()

plt.show()

##################### END: Part D #######################

##################### END: Section 1 #####################



##################### START: Section 2 #####################



#Generate the arrays to sort
numElements_ins = [1]   #initialized with 1 to make generation easier
arrN_ins = [[1], [], [], [], [], [], [], [], [], [], []]    #also initialized with 1

for i in range(1, 11):
    startVal = (i-1)*100 + 100
    for j in range(1, startVal + 1):
        arrN_ins[i].append(j)
    numElements_ins.append(startVal)
    # need to reverse the list now, it was added as a sorted list
    arrN_ins[i] = Reverse(arrN_ins[i])
    

timeTakenArr_ins = []   #empty array to store timing information

#Sort all the arrays, saving timing information
for arr in arrN_ins:
    # sleep for 1 second
    # Spyder likes to print while code is running, which can mess with timing information
    # This just helps ensure accurate information
    time.sleep(1)
    startTime = timer()
    
    insertionSort(arr)
    
    endTime = timer()
    print("Time taken to sort an array of " + str(len(arr)) + " elements in milliseconds: " + str((endTime - startTime) * 1000))
    timeTakenArr_ins.append((endTime - startTime) * 1000)
    
    
# Estimate time taken with formula: 0.5*(t*t) + (0.5*t) - 1
timeEst_ins = []
for i in range(len(numElements_ins)):
    timeEst_ins.append(0.5*(numElements_ins[i]*numElements_ins[i]) + 0.5*numElements_ins[i] - 1)

# Scale the estimates to match our measurements
scaleFactor = timeTakenArr_ins[10] / timeEst_ins[10]
for i in range(len(timeEst_ins)):
    timeEst_ins[i] = timeEst_ins[i] * scaleFactor
    

# plot the data
plt.scatter(numElements_ins, timeTakenArr_ins)
plt.xlabel("Number of elements in array vs time taken to sort (milliseconds) with Insertion Sort")
plt.ylabel("")
plt.title("Insertion Sort")
plt.show()

plt.scatter(numElements_ins, timeEst_ins)
plt.xlabel("Number of elements in array vs time taken to sort (milliseconds) with Insertion Sort")
plt.ylabel("")
plt.title("Insertion Sort time estimate assuming O((n^2)/2 + n^2 + 1) complexity")
plt.show()

plt.scatter(numElements_ins, timeTakenArr_ins)
plt.scatter(numElements_ins, timeEst_ins)
plt.xlabel("Number of elements in array vs time taken to sort (milliseconds) with Insertion Sort")
plt.ylabel("Blue: Measured time, Orange: Estimated time")
plt.title("Insertion Sort time compared with estimated time")
plt.show()

##################### END: Section 2 #####################



##################### START: Section 3 #####################

#Generate the arrays to sort   
numElements_merge = [1]   #initialized with 1 to make generation easier
arrN_merge = [[1], [], [], [], [], [], [], [], [], [], []]    #also initialized with 1

for i in range(1, 11):
    startVal = (i-1)*100 + 100
    for j in range(1, startVal + 1):
        arrN_merge[i].append(j)
    numElements_merge.append(startVal)
    # need to reverse the list now, it was added as a sorted list
    arrN_merge[i] = Reverse(arrN_merge[i])
    

timeTakenArr_merge = []   #empty array to store timing information

#sort all the arrays, maintaining timing information
for arr in arrN_merge:
    # sleep for 1 second
    # Spyder likes to print while code is running, which can mess with timing information
    # This just helps ensure accurate information
    time.sleep(1)
    
    startTime = timer()
    
    mergeSort(arr)
    
    endTime = timer()
    
    print("Time taken to sort an array of " + str(len(arr)) + " elements in milliseconds: " + str((endTime - startTime) * 1000))
    timeTakenArr_merge.append((endTime - startTime) * 1000)

# Estimate time taken with recursive formula: 𝑚𝑛 = 𝑚⌊𝑛/2⌋ + 𝑚⌈𝑛/2⌉ + (𝑛 − 1) for 𝑛 > 1 with 𝑚1 = 0
timeEst_merge = []
for i in range(len(numElements_merge)):
    timeEst_merge.append(mergeSortEstimate(numElements_merge[i]))

# Scale the estimates to match our measurements
scaleFactor = timeTakenArr_merge[10] / timeEst_merge[10]
for i in range(len(timeEst_ins)):
    timeEst_merge[i] = timeEst_merge[i] * scaleFactor



# plot the data
plt.scatter(numElements_merge, timeTakenArr_merge)
plt.xlabel("Number of elements in array vs time taken to sort (milliseconds) with Merge Sort")
plt.ylabel("")
plt.title("Merge Sort")
plt.show()

plt.scatter(numElements_merge, timeEst_merge)
plt.xlabel("Number of elements in array vs time taken to sort (milliseconds) with Merge Sort")
plt.ylabel("")
plt.title("Merge Sort time estimate assuming m(n) = m⌊n/2⌋ + m⌈n/2⌉ + (n − 1) for n > 1 with m(1) = 0")
plt.show()

plt.scatter(numElements_merge, timeTakenArr_merge)
plt.scatter(numElements_merge, timeEst_merge)
plt.xlabel("Number of elements in array vs time taken to sort (milliseconds) with Merge Sort")
plt.ylabel("Blue: Measured time, Orange: Estimated time")
plt.title("Merge Sort time compared with estimated time")
plt.show()

##################### END: Section 3 #####################
