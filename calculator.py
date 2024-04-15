import math
import re

i = 0
while i == 0:
    print("Enter first number: ")
    firstnum = int(input())
    print("Enter second number: ")
    secondnum = int(input())
    print("What do you want to do:\n 1. ADD\n 2. SUBSTRACT\n 3. MULTIPLY\n 4. DIVIDE\n 5. Exit")
    equation = input()
    answer = 0
    if equation == "1" or equation == "ADD" or equation == "Add" or equation == "add":
        answer = firstnum + secondnum
        print(answer)
    elif equation == "2" or equation == "SUBSTRACT" or equation == "Substract" or equation == "substract":
        answer = firstnum - secondnum
        print(answer)
    elif equation == "3" or equation == "MULTIPLY" or equation == "Multiply" or equation == "multiply":
        answer = firstnum * secondnum
        print(answer)
    elif equation == "4" or equation == "DIVIDE" or equation == "Divide" or equation == "divide":
        answer = firstnum / secondnum
        print(answer)
    else:
        print("Goodbye")
        exit()