"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    when the denominator or the numerator is nat an int

2. When will a ZeroDivisionError occur?
    when the denominator is 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    loop when a user enters a 0
"""

try:
    denominator = 0
    while denominator == 0:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("The denominator cannot be 0.")
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
