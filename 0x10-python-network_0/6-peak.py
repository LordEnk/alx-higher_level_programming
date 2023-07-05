#!/usr/bin/python3
"""contains the function find_peak"""

def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    li = list_of_integers
    l = len(li)

    if l == 0:
        return None

    left = 0
    right = l - 1

    while left < right:
        mid = (left + right) // 2

        if li[mid] < li[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return li[left]
