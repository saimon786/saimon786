"""py has  some data type & number type is one of them  
Python Numbers
There are three numeric types in Python:

int
float
complex
Variables of numeric types are created when you assign a value to them:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

"""


# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.




x =10 
b = 20
c = 12397349498493849832947 

# print (f'({x} :type  {type(x)} & {b} : type {type(b)} )') 

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.


x = 1.3
b = 2.4
c =-3.09

print (f"({x} :type  {type(x)} & {c} : type {type(b)}")


# Complex numbers are written with a "j" as the imaginary part: 

x = 1j
b = 0.1j
c = 3094085485j

# Type Conversion 
# You can convert from one type to another with the int(), float(), and complex() methods:
# Note: You cannot convert complex numbers into another number type.

x = 1 
y = 1.0
z = 1+2j 

# int to float 
print(float(x))
# floa to int 
print(int(y))
# int to complex 
print(complex(x))
# float to complex 
print(complex(y))


# Random Number 
# py has random number genaretor module 
import random
print(random.randint(1,10))
print(random.randrange())

