"""
CP1404/CP5632 Practical
list exercises
"""

# 1. Numbers stuff
number_of_inputs = 5
numbers = []
for i in range(number_of_inputs):
    number = int(input("Numbers: "))
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"the largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers)/len(numbers)}")

# 2. Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
             'ExecState', 'InteractiveConsole', 'InterpreterInterface',
             'StartServer', 'bob']
username = input("Enter username:")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")