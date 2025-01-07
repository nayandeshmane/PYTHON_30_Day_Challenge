def linear_search(arr, target):
    # Go through each item in the list
    for i in range(len(arr)):
        if arr[i] == target:  # Check if the current item matches the target
            return i  # Return the position if found
    return -1  # If not found, return -1

# Example usage
numbers = [10, 20, 30, 40, 50]
target = 30

result = linear_search(numbers, target)

if result != -1:
    print(f"Element {target} found at position {result}.")
else:
    print(f"Element {target} not found.")
