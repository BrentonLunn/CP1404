"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score not in range(0, 101):
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("passable")
elif score < 50:
    print("Bad")

