#!/usr/bin/env python
# coding: utf-8

# ### Name: Aakef Waris
# ### Email: awaris@hawk.iit.edu
# ### A-Number: A20420535
# ### Seat Number: 62
# 
# # Homework 2 Maximum Subarray Problem

## run this:
## python subarray.py


def findMaxSubArr(arr):
    # initial results
    hi = -999999
    endpts = ()
    
    ## Go through each index as a starting point - O(N)
    for start in range(len(arr)):
        total = 0
        ## Calculate the running sum from each start index to the end - O(N)
        for idx in range(start, len(arr)):
            total += arr[idx]
            ## if running total from start to current index is greater than hi
            ## then update hi and endpoints tuple - O(1)
            if total > hi:
                hi = total
                endpts = (start, idx)
    
    # function is O(N^2)
    # return original array, endpoints of max sub array, as well as sum of max sub array
    return arr, endpts, hi
            


# ## Tests for Python Code/Results




import random
tests = []
for _ in range(10):
    tests.append([ random.randrange(-999, 1000)for i in range(0,10)])
for i,test in enumerate(tests):
    print("Test " + str(i+1) + ":")
    print("")
    result = findMaxSubArr(test)
    print("Original Array :", result[0])
    print("Max Interval   :", result[1])
    print("Interval Sum   :", result[2])
    print("-----------------------------------------------------------------------------------------")
    print("")

