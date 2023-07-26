"""
MODULES. They are functionalities to can reuse.

In python there are many modules. You can see here:
https://docs.python.org/3/py-modindex.html

Also we can obtein modules from internet and finally
we can make our own mudules.

"""
"""
#Import module and use it

import mi_modulo


print(mi_modulo.HolaMundo("Hola Dei, buen dia"))
print(mi_modulo.calculadora(2,25, True))

"""

# Import a part of mi_modulo

from mi_modulo import HolaMundo

print(HolaMundo("Hola Dei, buen dia 2"))

#Module datetime (fechas)

import datetime

print(datetime.date.today())

complete_date = datetime.datetime.now()

print(complete_date)
print(complete_date.year)
print (complete_date.month)
print(complete_date.day)

personality_date = complete_date.strftime("%d/%m/%Y, %H:%M:%S")

print("Mi fecha personalizada:", personality_date)

#Module Math (Matematicas)

import math

print("The square root of 21: ", math.sqrt(21))

print("Pi number: ", float(math.pi))

print("Round a number: ", math.ceil(21.34597659))

#Module random
import random

print ("Random number between 21 and 73: ", random.randint(21,73))




















