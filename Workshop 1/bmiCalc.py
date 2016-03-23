print('Body-mass-index calculator, by Luke')

weight_value = float(input('Please enter your weight in kgs:'))
height_value = float(input('Please enter your height in m:'))


def calculate_bmi(weight, height):
    bmi_calculated = weight / height ** 2
    return bmi_calculated

bmi_value = calculate_bmi(weight_value, height_value)
print('Therefore, your BMI value is:', bmi_value)
print('thank you!')
