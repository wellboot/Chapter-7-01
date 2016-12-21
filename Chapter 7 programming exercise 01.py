# Exercise: Many companies pay time-and-a-half for
# any hours worked above 40 in a given week. Write a program to input
#  the number of hours worked and the hourly rate and calculate the total
# wages for the week


def main():

    hours = int(input("Enter the number of hours worked: "))
    wage_reg = int(input("Enter hourly pay: "))
    wage_over = wage_reg * 1.5

    # if statement to calculate weekly pay for 40 or less hours
    if hours <= 40:
        pay = wage_reg * hours
        print("Your weekly pay for ", hours," of work is ", pay)

    # else statement to calculate weekly pay for more than 40 hours
    else:
        pay = wage_over * hours
        print("Your weekly pay for ", hours, " of work is ", pay)



main()