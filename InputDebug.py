'''
InputDebug
Pawelski
10/1/2023
Introduction to Computer Science
'''

num1 = input("Enter a number >> ") # There is a bug on this line.
int(input("Enter another number >> ")) # There is a bug on this line.
product = num1 * num2 # This line causes an error because the last two lines have bugs.
print(str(num1) + " * " + str(num2) + " = " + str(product))
