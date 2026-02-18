"""
A simple command-line calculator that performs basic arithmetic
operations (+, -, *, /) step-by-step without applying operator precedence,
and prints the full expression with the final result.
"""

result = None
operand = None
operator = None
wait_for_number = True
calculator_running = True
sentence = ""

while wait_for_number:
    try:
        result = float(input("Enter a number: "))
        sentence = str(result)
        wait_for_number = False
    except ValueError:
        print("Not a number, try again")

while calculator_running:
    while wait_for_number:
        try:
            operand = float(input("Enter a number: "))
            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "*":
                result *= operand
            elif operator == "/":
                result /= operand
            wait_for_number = False
            sentence += str(operand)
        except ValueError:
            print("Not a number, try again")
        except ZeroDivisionError:
            print("Cannot divide by zero, try again")

    while not wait_for_number:
        operator = input("Enter operator (+ - * / =): ")
        if operator == "+":
            sentence += " + "
            wait_for_number = True
        elif operator == "-":
            sentence += " - "
            wait_for_number = True
        elif operator == "*":
            sentence += " * "
            wait_for_number = True
        elif operator == "/":
            sentence += " / "
            wait_for_number = True
        elif operator == "=":
            sentence += " ="
            print(sentence, result)
            calculator_running = False
            break
        else:
            print("Not operator (+ - * /), try again:")
