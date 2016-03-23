print('Temperature Conversion program')

celsius_value = float(input('Enter temperature in celsius:'))
kelvin_value = celsius_value + 273.15


def convert_celsius_to_fahrenheit(celsius_value):
    fahrenheit_value = celsius_value * 9 / 5 + 32
    return fahrenheit_value

fahrenheit_value = convert_celsius_to_fahrenheit(celsius_value)
print('celsius value:', celsius_value)
print('fahrenheit value:', fahrenheit_value)
print('kelvin value:', kelvin_value)
