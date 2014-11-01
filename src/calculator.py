#Ben Schwabe
#practice with python, for python 2.7
"""
calculator.py
"""


def processOperator(operator,num1,num2):
    #add
    if  operator == "add":
        return num1 + num2
    #subtract
    elif operator == "subtract":
        return num1 - num2
    
#control var for stopping program
done = False

#MAIN LOOP
while not done:
    #controls whether to process variables
    fail = False
    num1 = raw_input("first number or quit: ")
    try:
        num1 = float(num1)
    except:
        #not processing calculation
        fail = True
    if not fail:
		operator = raw_input("operation: ")
		operator = str(operator)
		
		num2 = raw_input("second number: ")
		num2 = float(num2)
    
    if not fail:
        print(processOperator(operator,num1,num2))
    else:
        done = True
