"""
Insertion Sort:

Insertion sort is a simple sorting algorithm that
Works by iteratively inserting each element of an unsorted list,
Into its correct position in a sorted portion of the list.
It is a stable sorting algorithm,
Meaning that elements with equal values
Maintain their relative order in the sorted output.

Time complexity: O(n ^ 2)
Space complexity: O(1)
"""
import time
from typing import List, Any, Tuple

def insertion_sort(list_: List[Any]) -> Tuple[List[Any], int]:
    steps = 0
    for i in range(1, len(list_)):
        steps += 1
        key = list_[i]
        j = i-1
        while j >= 0 and key < list_[j] :
            steps += 1 
            #Shift the element to make a gap.
            list_[j + 1] = list_[j]
            j -= 1
        list_[j + 1] = key

    return list_, steps

print("Insertion Sort Algorithm: \n")

unsorted_list = [30, 20, 18, 17, 15]
print("Unsorted: ", unsorted_list, "\n")

start = time.perf_counter()
sorted_list, steps = insertion_sort(unsorted_list)
end = time.perf_counter()

print(f"Time for {len(unsorted_list)} Elements is: {str(steps)}")
print("Sorted: ", sorted_list, "\n")