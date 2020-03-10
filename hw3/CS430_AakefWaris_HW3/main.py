
from Sort import SortingMachine
from Test import TestMachine, TestResults
import sys
sys.setrecursionlimit(15000)

if __name__ == "__main__":
    quickSortResults = TestResults("Quick Sort")
    heapSortResults = TestResults("Heap Sort")
    for test in TestMachine.createBatch():
        quickSortResults.addResult(TestMachine.timeIt(SortingMachine.heapSort, test))
        heapSortResults.addResult(TestMachine.timeIt(SortingMachine.quickSort, test))
    
    quickSortResults.visualize()
    heapSortResults.visualize()


