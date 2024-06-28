def calculate(equation):
    i = 0
    cur_num = 0
    operation = "+"
    result = 0 
    prev = 0

    while i < len(equation):
        # parse string
        while i < len(equation) and equation[i].isnumeric():
            cur_num = cur_num * 10 + int(equation[i])
            i += 1
        if operation == "+":
            result += cur_num
        elif operation == "-":
            result -= cur_num
        elif operation == "*":
            result *= cur_num
        elif operation == "/":
            result /= cur_num
        
        if i < len(equation):
            operation = equation[i] 
        
        cur_num = 0

        i += 1

    return result

def main():
    print("Welcome to the simple calculator!")
    equation = input ("Enter an equation to be solved: ")
    print(f"The equation is: {equation}")    
    result = calculate(equation)
    
    print(result)

        
    #num1 = float(input("Enter a value: "))
    #num2 = float(input("Enter another value: "))
    #operation = input("Enter an operation(+, -, *, /): ")

    #if operation == "+":
    #    result = num1 + num2
    #elif operation == "*":
    #    result = num1 * num2
    #elif operation == "-":
    #    result = num1 - num2
    #elif operation == "/":
    #    result = num1 / num2
    #else:
    #    print("Invalid operation was inputted.")
    
    #print(f"{num1} {operation} {num2} = {result}")


if __name__ == "__main__":
    main()

