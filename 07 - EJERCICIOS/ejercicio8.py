"""
Do a program where it have to calculate the percentage of a number.

"""

number = int(input("Intruduce a number: "))
percentage = int(input("Introduce a percentage: "))

if number >= 0 and percentage >= 0:
    operator = ((number*percentage)/100)
    print(f"El {percentage} %  de {number} es {operator}")
else:
    print("the introduced numbers must be major to 0")