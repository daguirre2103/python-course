"""
Write the square numbers since 1 to 60 with for and while.

"""

# for
for contador in range (1,61):
    print(f"{contador} x {contador} = {contador*contador}")


#while
contador2 = 1
while contador2 <= 60:
    print(f"{contador2} x {contador2} = {contador2*contador2}")
    contador2 += 1

