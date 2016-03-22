print('Body-mass-index calculator, by Luke')

weight_value = float(input('Please enter your weight in kgs:'))
height_value = float(input('Please enter your height in m:'))

bmi_value = weight_value / height_value ** 2

print('Therefore, your BMI value is:', bmi_value)
print('thank you!')
