# Leap Year Check
# Write a program to check whether a given year is a leap year.

year=int(input("Enter the year:"))
if year % 4 ==0 and year % 100 !=0 or year % 400 ==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not leap year")