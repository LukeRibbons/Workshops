DISCOUNT = 0.1
current_shipping_cost = 0

number_of_items = int(input('Enter how many items:'))
while number_of_items < 0:
    print('Invalid number of items!')
    number_of_items = int(input('Enter how many items:'))

for i in range(number_of_items):
    cost_of_item = float(input('Enter cost of item:'))
    current_shipping_cost += cost_of_item

if current_shipping_cost > 100:
    total_shipping_cost = current_shipping_cost - current_shipping_cost * DISCOUNT
else:
    total_shipping_cost = current_shipping_cost
print('The total shipping cost is:', '$' + str(total_shipping_cost))
