"""
Exponential Search

Given a sorted array, and an element x to be searched,
find the index of x in the array.

Input:  arr: List = [10, 20, 40, 45, 55]
        x = 45
Output: Element found at index 3

Input:  arr: List = [10, 15, 40, 45, 55]
        x = 15
Output: Element found at index 1


Exponential search involves two steps:  
    1- Find range where element is present
    2- Do Binary Search in above found range.


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


def exponential_search(array: List[Any], length: int, x: Any):
    if array[0] == x:
        return 0

    i = 1
    while i < length and array[i] <= x: #Loop until the right subarray
        i = i * 2

    return binary_search(array, i // 2, min(i, length - 1), x)


def create_list_with_n_elements(n: int) -> List:
    l = list(range(0, n))

    return l


array = create_list_with_n_elements(100)
x = 99
print(exponential_search(array, len(array), x))