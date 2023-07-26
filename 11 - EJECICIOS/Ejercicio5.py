"""
EXERCISE 5. You have to make a program that take the data of table and it order in a list and diccionary.

ACTION    ADVENTURE           SPORTS
GTA        ASSESINS CREP      FIFA 23
GOD        CRASH              PES 21 
PUGB       PRINCE OF PERSIA   MOTOGP 21
"""


tabla = [
    {
        "category": "ACTION",
        "games": ["GTA","GOD","PUGB"]
    },
    {
        "category": "ADVENTURE",
        "games" :["ASSSESINS CREED", "GRASH", "PRINCE OF PERSIA"]
    },
    {
        "category": "SPORTS",
        "games": ["FIFA 23", "PES 23", "MOTOGP 23" ]
    }
]

#You have to show this list with diccionaries and lists inside.

for categoria in tabla:
    print (f"--------------------{categoria['category']} -----------------------")
    for juego in categoria['games']:
        print (juego)
