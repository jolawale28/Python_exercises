# Write a program that generates a random number between 1 and 10 and prints your name
# that many times.

# 2023 Joseph Olawale Bamidele

import random as random_object

count = random_object.randint(1, 10)

for i in range(count):
    print(i + 1, "Joseph Olawale Bamidele")