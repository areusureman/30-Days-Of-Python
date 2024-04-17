age = 30
height = 23.1
complex_variable = 9 + 1j

#calculate area given a base and a height

user_base = input('Enter base: ')
user_height = input('Enter height: ')
user_area = (int(user_base) * int(user_height)) / 2
print( 'The area of the triangle is: ' ,  user_area)

#calculate perimeter of triangle given all 3 sides
user_side_a = input('Enter side a: ')
user_side_b = input('Enter side b: ')
user_side_c = input('Enter side c: ')
user_perimeter = int(user_side_a) + int(user_side_b) + int(user_side_c)
print( 'The perimeter of the triangle is: ' ,  user_perimeter')

#calculate area and perimeter of rectangle given length and width

user_length = input('Enter length: ')
user_width = input('Enter width: ')
user_area = int(user_length) * int(user_width)
user_perimeter = (int(user_length) + int(user_width)) * 2
print( 'The area of the rectangle is: ' ,  user_area)

#calculate area and circumference of a circle given the radius

user_radius = input('Enter radius: ')
user_area = 3.14 * (int(user_radius) ** 2)
user_circumference = 2 * 3.14 * int(user_radius)
print( 'The area of the circle is: ' ,  user_area)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2

"""
slope
2

x intercept
y=2x-2
0=2x-2
2=2x
x=1
(1,0)

y intercept
y= 2x-2
y= 0x -2
y= -2
(0,-2)

"""
