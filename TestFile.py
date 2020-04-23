# accepts only integer and float input from user
def is_num(value):
    while True:
        try:
            if isinstance(value, int):
                value = int(value)
                break
            elif isinstance(value, float):
                value = float(value)
                break
        except ValueError:
            print("Not a valid number. Please try again.")


# accepts only string input from user
def is_operator(value):
    while True:
        else:
            print("Not a valid operator. Please try again.")


print("Hello! Welcome to Joanne Calculator!")

user_num_1 = input("Please enter the first number: ")
is_num(user_num_1)

user_operator = input("Please enter the operator (+, -, *, /): ")
is_operator(user_operator)

user_num_2 = input("Please enter the second number: ")
is_num(user_num_2)

# need to fix; incorporate into function
if operator == "+":
    answer = num_1 + num_2
elif operator == "-":
    answer = num_1 - num_2
elif operator == "*":
    answer = num_1 * num_2
elif operator == "/":
    answer = num_1 / num_2

print("The answer is %s" % answer)
# print("The answer is ", answer)

# HW
# Create a main function
# Create a way for the user to use the program again
# Exceptions (try, ValueError, .isdigit())
# Project structure (readme, code folder, test folder)
# Differentiate between integer and float
