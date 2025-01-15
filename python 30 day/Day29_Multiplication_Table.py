# Generating Multiplication Tables
# Difficulty: Easy
# Topics: Basic Programming, Mathematical Computations
# Description: Write a program to generate multiplication tables for a given number.
# Input from user
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
