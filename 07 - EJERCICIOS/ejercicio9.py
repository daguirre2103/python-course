"""
Do a program that ask numbers indefinely to user until he intruduce 111

"""
contador = 1
while contador <= 100:
    number = int(input("Intruduce a number: "))
    if number == 111:
        break
    else:
        print (f"You intruduce the number {number}")
    contador += 1
    