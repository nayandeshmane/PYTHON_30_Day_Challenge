#Crafting Star Patterns
#Difficulty: Easy
#Topics: Basic Programming, Patterns
#Description: Write a program to create different star patterns (e.g., pyramid, diamond).
#Example:
#Input: patternType = "pyramid", height = 5
#Output:

 #   *
 #  ***
 # *****
# *******
#*********

def pyramid_pattern(height):
    for i in range(height): 
        spaces = ' ' * (height - i - 1)    
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
pyramid_pattern(5)
