while True:
   
    operator = input("Enter operation (+, -, *, /,!): ")
    if operator =="!":
        print("Calculator Closed")
        break
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    
    if operator == "+":
        print("Result:", num1 + num2)

    elif operator == "-":
        print("Result:", num1 - num2)

    elif operator == "*":
        print("Result:", num1 * num2)

    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero")
        else:
            print("Result:", num1 / num2)
 

    else:
        print("Invalid operator")
