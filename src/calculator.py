# created by: Ben Schwabe
# upgraded by: Bagdat Bimaganbetov
# practice with python, for python3
"""
calculator.py
"""
print("Welcome!")
print("I am a simple calculator.")

# available operators
operators = ["add", "subtract", "divide", "multiple"]

# control var for stopping program
done = False

def processOperator(operator, num1, num2):
    # add
    if operator == "add":
        return num1 + num2
    # subtract
    elif operator == "subtract":
        return num1 - num2
    # multiple
    elif operator == "multiple":
        return num1 * num2
    # divide
    elif operator == "divide":
        if num2 == 0:
            print("Watch out! You trying to open hell gates! Be careful!")
        else:
            return num1/num2

# MAIN LOOP
while not done:
    # controls whether to process variables
    fail = False
    num1 = input("Enter first number or any value to quit: ")
    try:
        num1 = float(num1)
    except ValueError:
        # not processing calculation
        fail = True
        print("Bye.")
    if not fail:

        operator = input("operation [add/subtract/divide/multiple]: ")
        if operator in operators:
            operator = str(operator)
        else:
            print("Operator not found. Please, try again")
            continue
        num2 = input("Second number: ")
        num2 = float(num2)

    if not fail:
        print("Result is:", processOperator(operator, num1, num2))
    else:
        done = True
