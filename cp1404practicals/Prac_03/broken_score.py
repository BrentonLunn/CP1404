"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    print(get_result(score))
    print(get_result(random.randint(0, 101)))


def get_result(score):
    if score not in range(0, 101):
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "passable"
    elif score < 50:
        result = "Bad"
    return result


main()
