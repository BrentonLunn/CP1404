"""
CP1404/CP5632 - Practical

"""

# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()
#
# for i in range(0,110, 10):
#     print(i, end=" ")
# print()
#
# for i in range(20, 0, -1):
#     print(i, end=" ")
# print()
#
# stars = int(input("Number of stars: "))
# for i in range(stars):
#     print("*", end="")

number_of_stars = 1
stars = int(input("Number of stars: "))
for i in range(stars):
    print("*" * number_of_stars)
    number_of_stars += 1
