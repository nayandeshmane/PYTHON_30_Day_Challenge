#Find Missing Number
#Given a list of n-1 numbers in the range from 1 to n, find the missing number.
#Example:
#Input: [1, 2, 4, 5]
#Output: 3
nums = [1, 2, 4, 5]
def find_missing_number(nums):
    #nums = [1, 2, 4, 5]
    n = len(nums) + 1  # Total numbers including the missing one
    total = n * (n + 1) // 2  # Total sum of numbers from 1 to n
    return total - sum(nums)  # Missing number

print("The missing number is:", find_missing_number(nums))
