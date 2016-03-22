print('Temperature Conversion program')


def convert_celsius_to_fahrenheit():
    celsius_value = float(input('Enter temperature in celsius:'))
    fahrenheit_value = celsius_value * 9 / 5 + 32
    kelvin_value = celsius_value + 273.15
    return celsius_value, fahrenheit_value, kelvin_value

temperature_tuple = convert_celsius_to_fahrenheit()
print('celsius value:', temperature_tuple[0])
print('fahrenheit value:', temperature_tuple[1])
print('kelvin value:', temperature_tuple[2])
