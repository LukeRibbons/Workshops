print('Area calculator')

depth = float(input('enter depth:'))
width = float(input('enter width:'))
height = float(input('enter height:'))


def calculate_area(width, height):
    rectangle_area = width * height
    return rectangle_area
area = calculate_area(width, height)
volume = area * depth

print('Area:', area, 'Volume:', volume)