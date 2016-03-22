print('Body-mass-index calculator, by Luke')


def calculate_bmi():
    weight_value = float(input('Please enter your weight in kgs:'))
    height_value = float(input('Please enter your height in m:'))
    bmi_calculated = weight_value / height_value ** 2
    return bmi_calculated

bmi_value = calculate_bmi()
print('Therefore, your BMI value is:', bmi_value)
print('thank you!')
