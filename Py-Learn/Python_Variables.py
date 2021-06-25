# """ Python Variables are containers for store data values. 
# Python has nocommand for declearing variables 
# A variable is created when the moment you first assign a value to it. 
# Variables do not need to be declared with any particular type, 
#  ... and can even change type after they have been set. """
# Variable names are case-sensitive

Example_variale = 4 
# print(Example_variale)

# type funteion 
ex = type(Example_variale)
# print(ex)

# If you want to specify the data type of a variable, this can be done with casting.

x = (str(4))
y = (int(4))
z = (float(4))

# print(x,y,z) 

# Variable names are case-sensitive
a=3
A='3'
# this are not same Variables 
#A will not overwrite a
print(id(a))
print(id(A))