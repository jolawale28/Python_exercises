# Ask the user to enter a temperature in Celsius.
# The program should print a message based on the temperature:
# • If the temperature is less than -273.15, print that the temperature is invalid because it is below absolute zero.
# • If it is exactly -273.15, print that the temperature is absolute 0.
# • If the temperature is between -273.15 and 0, print that the temperature is below freezing.
# • If it is 0, print that the temperature is at the freezing point.
# • If it is between 0 and 100, print that the temperature is in the normal range.
# • If it is 100, print that the temperature is at the boiling point.
# • If it is above 100, print that the temperature is above the boiling point

# 2023 Joseph Olawale Bamidele

temp_value = eval(input("Please enter temperature value: "))

if (temp_value > 100):
    print("Temperature is above boiling point.")
elif (temp_value == 100):
    print("Temperature is at boiling point.")
elif (0 < temp_value < 100):
    print("Temperature is at normal range.")
elif (temp_value == 0):
    print("Temperature is at freezing point.")
elif (-273.15 < temp_value < 0):
    print("Temperature is below freezing point.")
elif (temp_value == -273.15):
    print("Temperature is at absolute zero.")
elif (temp_value < -273.15):
    print("Temperature is invalid.")