print('Electricity bill estimator')

electricity_price = float(input('Enter cents per kWh:'))
electricity_use_daily = float(input('Enter daily use in kWh:'))
billing_days = float(input('Enter number of billing days'))

estimated_bill = billing_days * electricity_use_daily * electricity_price/100

print('Estimated bill:', '$' + str(estimated_bill))
