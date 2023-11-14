# Write a program that generates and
# prints 50 random integers, each between 3 and 6

# 2023 Joseph Olawale Bamidele

import random as random_number_object

for i in range(50):
    random_numb = random_number_object.randint(3,6)
    print(i + 1, random_numb)
