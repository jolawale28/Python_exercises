# Write a program that generates a random decimal number between 1 and 10 with two decimal
# places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00

# 2023 Joseph Olawale Bamidele

import random

random_decimal_number = round(random.uniform(1.00, 10.00), 2)

print(random_decimal_number)