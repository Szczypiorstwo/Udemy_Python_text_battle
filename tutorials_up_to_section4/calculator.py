'''
    Program: Magical Calculator
    (and this is multiline comment)

'''

import re

print("Our magica calculator")
print("Type quit to exit.\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter an equation:")
    else:
        equation = input(str(previous))

    if equation == "quit":
        print("Goodbye, Human!")
        run = False
    else:
        equation = re.sub('[a-zA-Z.,:()=" "]', '', equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        #print("You typed", previous)

while run:
    performMath()