"""
Obtein every numbers between two numbers that the user write in the program.
"""
#FOR

number1= int(input("Ingress the first number please: "))
number2= int(input("Ingress the second number please: "))

if number2 > number1:
    for contador in range (number1, number2):
        print (f"{contador}")
elif number2 < number1:
    number3 = int (input("Ingress a number higher than the first number please: "))
    for contador in range (number1, number3):
        print (f"{contador}")
    if number3 < number1:
        print("You don't ingress a correct number")
    

