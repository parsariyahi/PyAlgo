"""
Binary Search:

Binary Search is defined as a searching algorithm used in a sorted array,
By repeatedly dividing the search interval in half.

Conditions for when to apply Binary Search in a Data Structure:
    * The data structure must be sorted.
    * Access to any element of the data structure takes constant time.


Time complexity: O(log n)
Space complexity: O(1)
"""


from typing import List, Any


def binary_search(array: List[Any], low: int, high: int, x: Any):
    if high >= low:
        mid = low + (high - low) // 2

        if array[mid] == x:
            return x #Found the Element

        if  array[mid] > x:
            return binary_search(array, low, mid - 1, x) #Element is in lower range

        return binary_search(array, mid + 1, high, x) #Element is in higher range

    return -1


def create_list_with_n_elements(n: int) -> List:
    l = list(range(0, n))

    return l


array = create_list_with_n_elements(100000)
x = 128
print(binary_search(array, 0, len(array), x))