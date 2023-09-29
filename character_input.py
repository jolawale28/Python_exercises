'''
https://www.practicepython.org/

This program asks the user to enter their name and their age.
It prints out a message addressed to them that tells them the year that they
will turn 100 years old.

Joseph Olawale Bamidele
September 2023

'''

import datetime

name_of_user = input("Please enter your name: ")
age_of_user = int(input("How old are you? "))

present_year = (datetime.date.today()).year

year_of_birth = present_year - age_of_user
year_of_birth = 2023 - age_of_user

year_to_100 = year_of_birth + 100

print(name_of_user, " you will be 100 years old in ", year_to_100)
