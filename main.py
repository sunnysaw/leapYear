"""
In this code of section we will see about the logic behind how the program runs to check that the year is leap year is
or not.
________________________________________________________________________________________________________________________
Question : find the year is leap year or not ?
_______________________________________________
Approach : first take input from user then second step is comparing the number with 365 number, if the number is greater
           than 365 then the year is leap year otherwise it is not a leap year.
"""
A = int(input("Enter the number of days for finding the year is leap year or not : "))
if A == 366:
    print("this is a leap year.")

if A < 366:
    print("this is not a leap year.")

if A > 366:
    print("Invalid number enter by user.....!")






