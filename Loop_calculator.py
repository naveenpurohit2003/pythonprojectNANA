unit = input("Enter the unit in which you want to convert the Days like Hours, Minutes, Seconds")
def calculator(number_of_days):

    try:
        number_of_days = int(number_of_days)
        if number_of_days > 0 and unit == "Hours":
            return f" {number_of_days} Days are equal to  {number_of_days * 24} {unit} "
        elif number_of_days > 0 and unit == "Minutes":
            return f" {number_of_days} Days are equal to {number_of_days * 24 * 60} {unit} "
        elif number_of_days > 0 and unit == "Seconds":
            return f" {number_of_days} Days are equal to {number_of_days * 24 * 3600} {unit} "
        elif number_of_days == 0 and unit == "":
            return f" {number_of_days} Days should not be equal to zero"
    except ValueError:
            return f"{number_of_days} Value you have inserted is invalid"

number_of_days = ""
while number_of_days != "exit":
#number_of_days = [1,2,3,4,5,6,7,8,9,10]
 number_of_days = input("Enter the number of days in comma spearated values that you wish to convert")
 for i in number_of_days.split(","):  #Split takes input as 10 20 30 and convert it to list [10, 20, 30]
  print(calculator(i))

