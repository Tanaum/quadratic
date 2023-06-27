#ax2 + bx + c = 0
from math import sqrt

print('NOTE: IF THERE IS NO NUMBER A VARIABLE, JUST WRITE 1 ALONG WITH WHATEVER SIGN IT HAS')
print("IF ONE OF THE VARIABLES JUST ISN'T GIVEN WRITE 0 IN ITS PLACE")

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

x1 = ((-1*b) + sqrt((b ** 2) - (4*a*c))) / 2*a

x2 = ((-1*b) - sqrt((b ** 2) - (4*a*c))) / 2*a
print(f'{x1:.2f}, {x2:.2f}')