#Ben Schwabe
#practice with python, for python 2.7
"""
calculator.py
"""


def processOperator(operator,num1,num2):
	#add
	if  (operator == "add"):
		return num1 + num2
	#subtract
	elif (operator == "subtract"):
		return num1 - num2
	
#control var for stopping program
done = False

#MAIN LOOP
while not done:
    num1 = raw_input("first number: ")
    num1 = float(num1)

    operator = raw_input("operation: ")
    operator = str(operator)
    
    num2 = raw_input("second number: ")
    num2 = float(num2)
    
    print(processOperator(operator,num1,num2))
