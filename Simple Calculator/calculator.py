print("******************* Welcome to Simple Calculator ****************************")
ans = 0

while(True):
    op = input("Enter the operator: ")
    
    if (op == '+' or op == '-' or op == '*' or op == '/' or op == '%'):
        num1 = int(input("Enter the number1: "))
        num2 = int(input("Enter the number2: "))

        if (op == '+'):
            ans = num1 + num2
            print(f'The addition of {num1} and {num2} is {ans}')
        if (op == '-'):
            ans = num1 - num2
            print(f'The Subtraction of {num2} from {num1} is {ans}')
        if (op == '*'):
            ans = num1 * num2
            print(f'The product of {num1} and {num2} is {ans}') 
        if (op == '/'):
            ans = num1 / num2
            print(f'The division of {num1} and {num2} is {ans}')
        if (op == '%'):
            ans = num1 % num2
            print(f'The modulo of {num1} and {num2} is {ans}')
    elif (op == 'x' or op == 'X'):
        break
    else:
        print("Invalid Operation!!")
