def calculator():
    while True:
        # Print options for the user
        print("Enter '+' to add two numbers")
        print("Enter '-' to subtract two numbers")
        print("Enter '*' to multiply two numbers")
        print("Enter '/' to divide two numbers")
        print("Enter 'quit' to end the program")
user_input = input(": ")
if user_input == "quit":
   break
elif user_input in ["+", "-", "*", "/"]:
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))
if user_input == "+":
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif user_input == "-":
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif user_input == "*":
    result = num1 * num2
    print(num1, "*", num2, "=", result)
elif user_input == "/":
    result = num1 / num2
    print(num1, "/", num2, "=", result)
else:
    print("Invalid Input")
calculator()
