# Count Frequency of Elements
# Write a Python program to count the frequency of each element in a list.
# Example:
# Input: [1, 2, 2, 3]
# Output: {1: 1, 2: 2, 3: 1}
input_list = [1, 2, 2, 3]
def count_frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1  # Increment count if item exists
        else:
            frequency[item] = 1  # Set count to 1 if item is new
    return frequency


#input_list = [1, 2, 2, 3]
output = count_frequency(input_list)
print(output)
