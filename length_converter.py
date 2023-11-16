# Write a program that asks the user to enter a length in centimeters. If the user enters a negative
# length, the program should tell the user that the entry is invalid. Otherwise, the program
# should convert the length to inches and print out the result. There are 2.54 centimeters in an inch

# 2023 Joseph Olawale Bamidele

length = eval(input("Please enter length in centimeters: "))

if (length < 0):
    print("Value is invalid. Please enter a value greater than zero!")
else:
    print("Centimeter: ", length, " | Inches: ", length/2.54)