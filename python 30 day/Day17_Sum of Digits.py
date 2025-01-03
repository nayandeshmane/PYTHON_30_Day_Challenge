# Sum of Digits
# Write a Python program to calculate the sum of digits of a given number.
# Example:
# Input: 1234
# Output: 10

num=1234
Sum_of_num=0
for i in str(num):
    Sum_of_num += int(i)
print(Sum_of_num)
    