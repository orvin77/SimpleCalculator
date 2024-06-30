''' 
Calculates the result of the inputted equation using PEMDAS 
'''
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
            prev = cur_num
        elif operation == "-":
            result -= cur_num
            prev = -cur_num
        elif operation == "*":
            result -= prev
            prev *= cur_num
            result += prev
        elif operation == "/":
            result -= prev
            prev /= cur_num
            result += prev
        
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

if __name__ == "__main__":
    main()
