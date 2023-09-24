# def calculator(number_of_days):
#     unit = input("Enter the unit which you want to change days to ")
#     try:
#             number_of_days = int(number_of_days)
#             if number_of_days >= 0 and unit == "Hours":
#                 return f"The {number_of_days} Days are equal to {number_of_days * 24} {unit}"
#             elif number_of_days >= 0 and unit == "Minutes":
#                 return f"The {number_of_days} Days are equal to {number_of_days * 24 * 60} {unit}"
#             elif number_of_days >= 0 and unit == "Seconds":
#                 return f"The {number_of_days} Days are equal to  {number_of_days * 24 * 3600} {unit}"
#     except ValueError:
#             return f"The Value {number_of_days}  is invalid"
#
# number_of_days = ""
# while number_of_days != "exit":
#  number_of_days = input("enter the number of day you want to convert")
#  A = calculator(number_of_days)
#  print(A)

#####################LIST Unfolding##############################

# A = ["Ramesh", "Suresh", "Dinesh"]
# B = ["Doctor", "Lawyer", "Teacher"]
#
# for i in A:
#  for j in B:
#      print(f"{i} is {j}")

unit = input("Enter the unit as Hours, Minutes, Seconds")
def calculator (number_of_days):

    number_of_days_int = number_of_days
    try:
            number_of_days = int(number_of_days)

            if unit == "Hours":
                print (f" {number_of_days} days are {number_of_days * 24} {unit}")
            elif unit == "Minutes":
                print (f" {number_of_days} days are {number_of_days * 24 * 60} {unit}")
            elif unit == "Seconds":
                print (f" {number_of_days} days are {number_of_days * 24 * 3600} {unit}")



    except ValueError:
       print(f"entered value {number_of_days_int} days is invalid")

    try:
     if unit == "Hours":
        return f" {number_of_days} days are {number_of_days * 24} {unit}"
     elif unit == "Minutes":
        return f" {number_of_days} days are {number_of_days * 24 * 60} {unit}"
     elif unit == "Seconds":
        return f" {number_of_days} days are {number_of_days * 24 * 3600} {unit}"

    except (ValueError):
        print(f"enter a valid value")

def validate_and_execute(user_input):
   try: #Try instead of if
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculator(user_input_number)
        elif user_input_number == 0:
            print("you entered a zero, Please enter a positive number")

   except ValueError: #Except instead of else to catch the value error
            print("you have entered an invalid input")


user_input = [1,2,3,4,5,6,7,8,9,10]        #list input
for num_days in user_input:
 calculator(num_days)