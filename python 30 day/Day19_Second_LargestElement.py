# Find Second Largest Element
# Write a program to find the second largest element in a list.
# Example:
# Input: [4, 2, 7, 1]
# Output: 4

def find_second_largest(nums):
    nums = list(set(nums))  
    nums.sort() 
    if len(nums) < 2:
        return "List must have at least two unique elements."
    return nums[-2]  # Return the second last element

# Example usage
input_list = [4, 2, 7, 1]
output = find_second_largest(input_list)
print("Second largest element:", output)
