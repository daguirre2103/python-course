"""
A set is a type of data, it is to have a collection of values, but without an index and an order.

"""
#Example 1

personas = {
    "david",
    "Flavia",
    "Santiago",
    "Mateo"
}

print(personas)

personas.add("Milka")
personas.remove("Santiago")

print(personas)

personas.add("Santiago")

print(personas)