print('Electricity bill estimator 2.0')

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

is_tariff_correct = False

while not is_tariff_correct:
    selected_tariff = input('Which tariff? 11 or 31:')
    if selected_tariff == '31':
        tariff_value = TARIFF_11
        is_tariff_correct = True
    elif selected_tariff == '11':
        tariff_value = TARIFF_31
        is_tariff_correct = True
    else:
        print('You have not entered 31 or 11 please try again')

electricity_use_daily = float(input('Enter daily use in kWh:'))
billing_days = float(input('Enter number of billing days:'))

estimated_bill = billing_days * electricity_use_daily * tariff_value

print('Estimated bill:', '$' + str(estimated_bill))

