def main():
    print("Welcome to the simple calculator!")

    num1 = float(input("Enter a value: "))
    num2 = float(input("Enter another value: "))
    operation = input("Enter an operation(+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Invalid operation was inputted.")
    
    print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()

