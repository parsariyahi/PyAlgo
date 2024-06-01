"""
Selection Sort:

Selection sort is a sorting algorithm that selects the smallest element,
From an unsorted list, in each iteration,
Places that element at the beginning of the unsorted list.

Time complexity: O(n ^ 2 / 2) wich is O(n ^ 2)
Space complexity: O(1)
"""
import time
from typing import List, Any, Tuple

def selection_sort(list_: List[Any]) -> Tuple[List[Any], int]:
    steps = 0
    for indx in range(len(list_)):
        min_indx = indx
        for i in range(indx+1, len(list_)):
            steps += 1
            if list_[i] < list_[min_indx]:
                min_indx = i
                steps += 1

        list_[indx], list_[min_indx] = list_[min_indx], list_[indx]

    return list_, steps


print("Selection Sort Algorithm: \n")

unsorted_list = [30, 20, 18, 17, 15]
print("Unsorted: ", unsorted_list, "\n")

start = time.perf_counter()
sorted_list, steps = selection_sort(unsorted_list)
end = time.perf_counter()

print(f"Time for {len(unsorted_list)} Elements is: {str(steps)}")
print("Sorted: ", sorted_list, "\n")