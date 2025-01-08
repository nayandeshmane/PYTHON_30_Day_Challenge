# #Binary Search
# Implement binary search to find an element in a sorted list.

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the middle
        if arr[mid] == target:     # Found the number
            return mid
        elif arr[mid] < target:    # Look in the right half
            left = mid + 1
        else:                      # Look in the left half
            right = mid - 1

    return -1  # Number not found

