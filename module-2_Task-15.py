result = None
operand = None
operator = None
wait_for_number = True

while wait_for_number:
    try:
        operand = float(input("Enter your number: "))
        result = operand
        print(operand)
        break
    except ValueError:
        print("Enter a number! ")


while True:
    operator = input("Enter an operator (/ * + -) or (=): ")
    
    if operator == "*":

        while wait_for_number:
            try:
                operand = float(input("Enter your number: "))
                result = result * operand
                print(operand)
                break
            except ValueError:
                print("Enter a number! ")

    elif operator == "+":

        while wait_for_number:
            try:
                operand = float(input("Enter your number: "))
                result = result + operand
                print(operand)
                break
            except ValueError:
                print("Enter a number! ")

    elif operator == "-":

        while wait_for_number:
            try:
                operand = float(input("Enter your number: "))
                result = result - operand
                print(operand)
                break
            except ValueError:
                print("Enter a number! ")

    elif operator == "/":

        while wait_for_number:
            try:
                operand = float(input("Enter your number: "))
                if operand == 0:
                    print("You cannot devide by zero!")
                    continue
                else:
                    result = result / operand
                    print(operand)
                    break
            except ValueError:
                print("Enter a number! ")

    elif operator == "=":
        print(result)
        break

    else:
        print(f"{operator} is not (/ * + - =)")
        


    
    
    
