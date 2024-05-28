"""
Linear Search:

Linear Search is defined as a sequential search algorithm,
That starts at one end and goes through each element of a list,
Until the desired element is found, otherwise the search continues till the end of the data set.

Linear Search Algorithm:

    * Every element is considered as a potential match for the key and checked for the same.
    * If any element is found equal to the key, the search is successful and the index of that element is returned.
    * If no element is found equal to the key, the search yields “No match found”.


Time complexity: O(n)
Space complexity: O(1)
"""


from typing import List, Any


def linear_search(array: List[Any], lentgh, x):
    for i in range(0, lentgh):
        if array[i] == x:
            return i

    return -1


def create_list_with_n_elements(n: int) -> List:
    l = list(range(0, n))

    return l


array = create_list_with_n_elements(100000)
x = 9999
print(linear_search(array, len(array) - 1, x))