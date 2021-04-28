# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 2021

@author: Aidan Becker and Abrar Ahmad
"""

import matplotlib.pyplot as plt
from timeit import default_timer as timer

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

################### START: Clearing charts from memory ######################

# I believe this is only necessary if the program is run multiple times in succession
# Almost no performance impact, can't really hurt though
# Might as well leave it in
plt.close('all')

################### END: Clearing charts from memory ######################

##################### START: Generate arrays to sort #####################

numElements = [1]   #initialized with 1 to make generation easier
arrN = [[1], [], [], [], [], [], [], [], [], [], []]    #also initialized with 1

for i in range(1, 11):
    startVal = (i-1)*100 + 100
    for j in range(1, startVal + 1):
        arrN[i].append(j)
    numElements.append(startVal)
    # need to reverse the list now, it was added as a sorted list
    arrN[i] = Reverse(arrN[i])
    
##################### END: Generate arrays to sort #####################

##################### START: Sort the arrays #####################

timeTakenArr = []   #empty array to store timing information

for arr in arrN:
    startTime = timer()
    
    insertionSort(arr)
    
    endTime = timer()
    print("Time taken to sort an array of " + str(len(arr)) + " elements in milliseconds: " + str((endTime - startTime) * 1000))
    timeTakenArr.append((endTime - startTime) * 1000)

# plot the data
plt.scatter(numElements, timeTakenArr)
plt.xlabel("Number of elements in the array")
plt.ylabel("Time taken to sort (milliseconds)")
plt.title("Number of elements vs time taken to sort with insertion sort")
plt.show()

##################### END: Sort the arrays #####################