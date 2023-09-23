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

A = ["Ramesh", "Suresh", "Dinesh"]
B = ["Doctor", "Lawyer", "Teacher"]

for i in A:
 for j in B:
     print(f"{i} is {j}")
