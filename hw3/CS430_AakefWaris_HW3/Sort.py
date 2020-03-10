import dataStructures.Trees as trees
class SortingMachine:


    @staticmethod
    def quickSort(arr,low=None,high=None):
    
       def partition(arr,low,pivot): 
           i = low-1          
           pVal = arr[pivot]      
    
           for j in range(low , pivot): 
               if arr[j] < pVal:  
                   i = i+1 
                   arr[i],arr[j] = arr[j],arr[i] 
    
           arr[i+1],arr[pivot] = arr[pivot],arr[i+1] 
           return i+1
    
       low = (0 if low is None else low)
       high = (len(arr)-1 if high is None else high)
    
       if low < high: 

           p = partition(arr,low,high) 
           SortingMachine.quickSort(arr, low, p-1) 
           SortingMachine.quickSort(arr, p+1, high)

       return arr
    
    @staticmethod
    def heapSort(arr):
        storage = trees.Heap(lambda x:-x)
        for i in arr:
            storage.add(i)
        lst = []
        while storage:
            lst.append(storage.pop())
        return lst
