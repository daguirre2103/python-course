'''
calculation_to_units=24
name_of_units="hours"

def days_to_units(num_of_days, custom_message):
    print (f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}")
    print(custom_message)

days_to_units(20, "hola")
days_to_units(35, "David")
days_to_units(48, "Flavia")
days_to_units(110, "Santi y Mateo")

'''
########### - LISTA ESTATICA - ####################################
'''
calculation_to_units=24
name_of_units="hours"
list = [10, 15, 20, 25, 30]

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"
    #print(custom_message)

for numero in list:
    result = days_to_units(numero)
    print(result)

'''

############ - LISTA DINAMICA - ######################################

'''
calculation_to_units=24
name_of_units="hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"


def validate_and_execute():
    try:
        num_of_days = int(user_input_element)      
        if num_of_days > 0:
            result = days_to_units(num_of_days)
            print(result)
        elif num_of_days == 0:
            print("Please introduce a positive number,try again")
        else:
            print("Please introduce a positive number,try again")
    except ValueError:
        print("You entered a wrong number, the program don't run")    

user_input = ""
while user_input != "exit":
    user_input = input ("Please introduce a number:\n")
    for user_input_element in user_input.split():
        validate_and_execute()'''

#Split is a function that convert a string to a list. For default "()" the strings has to be separate for a space but you can configurate a simbol, for example:
# .split(;)

################# SETS ##################################################

'''
calculation_to_units=24
name_of_units="hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"


def validate_and_execute():
    try:
        num_of_days = int(user_input_element)      
        if num_of_days > 0:
            result = days_to_units(num_of_days)
            print(result)
        elif num_of_days == 0:
            print("Please introduce a positive number,try again")
        else:
            print("Please introduce a positive number,try again")
    except ValueError:
        print("You entered a wrong number, the program don't run")    

user_input = ""
while user_input != "exit":
    user_input = input ("Please introduce a number:\n")
    
    list_of_days = user_input.split()
    print(list_of_days)
    print(set(list_of_days))
    print(type(list_of_days))
    print(type(set(list_of_days)))

    # Set doesn't allow elements duplicated.
    for user_input_element in set(list_of_days):
        validate_and_execute()
'''

# ------------------------------------------------------------------------
'''
my_set = { "January", "February", "March", "April"}
for element in my_set:
    print(element)

#Add element to a set

my_set.add("May")
print(my_set)

#Remove element to a set
my_set.remove("January")
print(my_set)

#Remove element to a list
my_list = [ "January", "February", "March", "April"]
my_list.remove("April")
print(my_list)
'''
############# functions ##########################################
'''
"david".center
"2, 3".split()
[1, 2, 4].count
'''
############# Diccionaries #######################################

'''
def days_to_units(num_of_days, name_of_units):
    if name_of_units == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {name_of_units}"
    elif name_of_units == "minutes":
        return f"{num_of_days} days are {num_of_days * 24*60} {name_of_units}"

def validate_and_execute():
    try:
        num_of_days = int(days_and_unit_diccionary["days"])      
        if num_of_days > 0:
            result = days_to_units(num_of_days, days_and_unit_diccionary["unit"])
            print(result)
        elif num_of_days == 0:
            print("You introduced a number equal 0")
        else:
            print("You introduced a wrong number")
    except ValueError:
        print("You entered a wrong number, the program don't run")    

user_input = ""
while user_input != "exit":
    user_input = input ("Please introduce a number of days and conversion unit:\n")
    days_and_unit = user_input.split(":")
    
    days_and_unit_diccionary = {
        "days": days_and_unit[0],
        "unit": days_and_unit[1]
        }
    
    print(days_and_unit_diccionary)
    validate_and_execute()
'''    

############################## Modules #################################

'''
import helper

user_input = ""
while user_input != "exit":
    user_input = input ("Please introduce a number of days and conversion unit:\n")
    days_and_unit = user_input.split(":")
    
    days_and_unit_diccionary = {
        "days": days_and_unit[0],
        "unit": days_and_unit[1]
        }
    
    print(days_and_unit_diccionary)
    helper.validate_and_execute(days_and_unit_diccionary)
'''

#How to import only some functions and variable from a module.

'''    
from helper import validate_and_execute, user_input_message

user_input = ""
while user_input != "exit":
    user_input = input (user_input_message)
    days_and_unit = user_input.split(":")
    
    days_and_unit_diccionary = {
        "days": days_and_unit[0],
        "unit": days_and_unit[1]
        }
    
    print(days_and_unit_diccionary)
    validate_and_execute(days_and_unit_diccionary)
'''

# How to change the name of module in the importation. 

'''
import helper as h

user_input = ""
while user_input != "exit":
    user_input = input (h.user_input_message)
    days_and_unit = user_input.split(":")
    
    days_and_unit_diccionary = {
        "days": days_and_unit[0],
        "unit": days_and_unit[1]
        }
    
    print(days_and_unit_diccionary)
    h.validate_and_execute(days_and_unit_diccionary)
'''

# How to use or built modules
# There are many modules already created from others

import os

print(os.name)




