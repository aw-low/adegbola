first_number = int(input("Inp first number."))

operation = input("Input operation")

second_number = int(input("Inp second number."))

list_operation = ["+","-","*","/"]


if operation in list_operation:
    print(first_number + second_number)
elif operation in list_operation:
    print(first_number - second_number)
elif first_number in list_operation:
    print(first_number * second_number)
else:
    print("Error in operation input")
