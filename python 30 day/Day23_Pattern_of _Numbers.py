# Generating a Pattern of Numbers
# Difficulty: Easy
# Topics: Basic Programming, Patterns
# Description: Write a program to generate number patterns (e.g., sequential numbers in a matrix).
# Example:
# Input: rows = 3

rows = int(input("Enter the number of rows: "))
num = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
