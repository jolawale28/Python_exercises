# Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit,
# the temperature is in. Your program should convert the temperature to the other unit.
# The conversions are F = (9/5)C + 32 and C = 5/9*(F − 32)

# 2023 Joseph Olawale Bamidele

temp_value = eval(input("Please enter temperature value: "))

from_unit = input("Please specify unit (Celsius/Fahrenheit): ")

if (from_unit == 'Celsius'):
    to_unit = 'Fahrenheit'
    converted_unit = (9 / 5) * temp_value + 32
else:
    to_unit = 'Celsius'
    converted_unit = (temp_value - 32) * 5 / 9

print("Convert ", temp_value, from_unit, " to ", to_unit)

print(temp_value, from_unit, " = ", converted_unit, to_unit)