import sys

print("Hola Mundo!")
print(sys.version)

# Indentation is important in python

"""
This is a multiline comment"
as you can see"
it is written in more
than just one line.
"""

if 5>2:
    print("5 es mayor a 2")

x = str("Monterrey")
print(x)

z = float(3.1416)
x = 5
x = "Juan"
print("x="+x, "z=",z)

# Error print(x+z)

print(type(x))
print(type(z))

x = 'Monterrey'
X = "Pachuca"
print(x, X)

# Camel case
miVariable = 'valor'

# Pascak case
MiVariable = 654

# Snake case
my_variable_nombre = "Gabriel"

_mes = 6

x, y , z = 'equis', "ye", "zeta"
print(x,y,z)

x = y = z 
print(x,y,z)

x = y = z = 2025
print(x,y,z)

frutas = [ "Manzana", "Pera", "Fresa" ]
x = y = z = frutas
print(x,y,z)

x, y, z = frutas
print(x,y,z)

w = "Chabacano"

def miFuncion():
    global w 
    w = "Durazno"
    z = 'Mango'
    print(w,x,y,z)

miFuncion()

print(w,z)