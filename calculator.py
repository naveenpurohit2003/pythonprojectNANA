
def calculator (number_of_days):
    unit = input("Enter the unit as Hours, Minutes, Seconds")
    number_of_days_int = number_of_days
    try:
        number_of_days = int(number_of_days)

    except ValueError:
        return f"entered value {number_of_days_int} days is invalid"

    try:
     if unit == "Hours":
        return f" {number_of_days} days are {number_of_days * 24} {unit}"
     elif unit == "Minutes":
        return f" {number_of_days} days are {number_of_days * 24 * 60} {unit}"
     elif unit == "Seconds":
        return f" {number_of_days} days are {number_of_days * 24 * 3600} {unit}"

    except (ValueError):
        print(f"enter a valid value")

def validate_and_execute():
   try: #Try instead of if
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculator(user_input_number)
        elif user_input_number == 0:
            print("you entered a zero, Please enter a positive number")

   except ValueError: #Except instead of else to catch the value error
            print("you have entered an invalid input")
user_input = input ("Hey user, enter a number of days and I will convert it to given unit")

A = calculator(user_input)
print(A)