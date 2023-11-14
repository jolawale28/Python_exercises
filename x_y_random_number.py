# Write a program that generates a random number, x, between 1 and 50, a random number y
# between 2 and 5, and computes x^y

# 2023 Joseph Olawale Bamidele

import random as random_number_object

x = random_number_object.randint(1, 50)
y = random_number_object.randint(2, 5)

print("x = ", x, ", y = ", y , ", x ** y = " , x ** y)