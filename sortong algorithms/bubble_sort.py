"""
Bubble Sort:

Bubble Sort is the simplest sorting algorithm,
That works by repeatedly swapping the adjacent elements,
If they are in the wrong order. 


Time complexity: O(n ^ 2)
Space complexity: O(1)
"""
import time
from typing import List, Any, Tuple

def bubble_sort(list_: List[Any]) -> Tuple[List[Any], int]:
    steps = 0
    for indx in range(len(list_)-1):
        for j in range(indx + 1, len(list_)):
            steps += 1
            if list_[indx] > list_[j]:
                list_[indx], list_[j] = list_[j], list_[indx]
                steps += 1

    return list_, steps


unsorted_list = [30, 20, 18, 17, 15, 10, 8, 6, 3, 2]

start = time.perf_counter()
sorted_list, steps = bubble_sort(unsorted_list)
end = time.perf_counter()

print("Bubble Sort Algorithm: \n")
print(f"Time for {len(unsorted_list)} Elements is: {str(steps)}")
print("Unsorted: ", unsorted_list, "\n")
print("Sorted: ", sorted_list, "\n")