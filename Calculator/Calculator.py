# list of accepted operators
operatorsList = ["+", "-", "*", "/"]


# accepts only integer and float input from user
def convert_num(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            raise ValueError


# calculation using two numbers and one operator
def calculate(operator, num_1, num_2):
    answer = 0
    if operator == "+":
        answer = num_1 + num_2
    elif operator == "-":
        answer = num_1 - num_2
    elif operator == "*":
        answer = num_1 * num_2
    elif operator == "/":
        answer = num_1 / num_2
    else:
        print("Error while calculating...")

    print("The answer is %s" % answer)


# Calculator simulation
def calc_simulation():
    print("Hello! Welcome to Joanne Calculator!")
    user_calc = "Y"

    while user_calc == "Y":
        while True:
            try:
                user_num_1 = input("Please enter the first number: ")
                num_1 = convert_num(user_num_1)
                break
            except ValueError:
                print("Not a valid number. Please try again.")

        while True:
            user_operator = input("Please enter the operator (+, -, *, /): ")
            if user_operator in operatorsList:
                break
            else:
                print("Not a valid operator. Please try again.")

        while True:
            try:
                user_num_2 = input("Please enter the second number: ")
                num_2 = convert_num(user_num_2)
                break
            except ValueError:
                print("Not a valid number. Please try again.")

        calculate(user_operator, num_1, num_2)

        user_calc = input("Would you like to make another calculation (Y/N)? ")
        while True:
            if user_calc == "Y" or user_calc == "N":
                break
            else:
                user_calc = input("Please enter Y/N: ")

    print("Thank you for using Joanne Calculator! See you next time!")


def main():
    calc_simulation()


if __name__ == "__main__":
    main()
