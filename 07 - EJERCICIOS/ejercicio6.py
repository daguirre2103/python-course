"""
Show every multiplication's table since 1 to 10.
"""

contador = 1
while contador <= 10:
    print (f"Multiplication's table of {contador}")
    for number in range (1, 11):
        print (f"{contador} x {number} = {contador*number}")
    contador += 1
    
               