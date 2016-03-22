print('Area calculator')

depth = float(input('enter depth:'))


def calculate_area():
    width = float(input('enter width:'))
    height = float(input('enter height:'))
    rectangle_area = width * height
    return rectangle_area
area = calculate_area()
volume = area * depth

print('Area:', area, 'Volume:', volume)