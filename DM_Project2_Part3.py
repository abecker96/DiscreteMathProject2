# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 2021

@author: Aidan Becker and Abrar Ahmad
"""

import matplotlib.pyplot as plt
from timeit import default_timer as timer

# Python program for implementation of MergeSort
# from: https://www.geeksforgeeks.org/merge-sort/
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
   
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
    
    mergeSort(arr)
    
    endTime = timer()
    print("Time taken to sort an array of " + str(len(arr)) + " elements in milliseconds: " + str((endTime - startTime) * 1000))
    timeTakenArr.append((endTime - startTime) * 1000)

# plot the data
plt.scatter(numElements, timeTakenArr)
plt.xlabel("Number of elements in the array")
plt.ylabel("Time taken to sort (milliseconds)")
plt.title("Number of elements vs time taken to sort with merge sort")
plt.show()


##################### END: Sort the arrays #####################