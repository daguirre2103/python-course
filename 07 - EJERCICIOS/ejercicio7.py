"""
Do a program that show every impare numbers between two numbers selected for a user.

"""

number1 = int(input ("Intruduce a first number: "))
number2 = int(input ("Intruduce a first number: "))

if number1 < number2:
    for contador in range (number1, number2):
        if contador % 2 != 0:
            print (f"el {contador} es IMPAR")
        else:
            print (f"el {contador} es PAR")
else:
    print ("Intruduced a wrong number")


