print("Hello! Welcome to Joanne Calculator.")

# need to include error messages for wrong inputs
num1 = float(input("Please enter the first number: "))
operator = input("Please enter the operator (+, -, *, /): ")
num2 = float(input("Please enter the second number: "))

if operator == "+":
    answer = num1 + num2
elif operator == "-":
    answer = num1 - num2
elif operator == "*":
    answer = num1 * num2
elif operator == "/":
    answer = num1 / num2

print("The answer is %s" % answer)
# print("The answer is ", answer)
