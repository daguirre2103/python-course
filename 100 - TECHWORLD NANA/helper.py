def days_to_units(num_of_days, name_of_units):
    if name_of_units == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {name_of_units}"
    elif name_of_units == "minutes":
        return f"{num_of_days} days are {num_of_days * 24*60} {name_of_units}"

def validate_and_execute(days_and_unit_diccionary):
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

user_input_message = "Please introduce a number of days and conversion unit:\n"