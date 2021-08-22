"""
CP1404/CP5632 - Practical
A shop requires a small program that
would allow them to quickly work out the total price
for a number of items, each with different prices.

"""


def main():
    total = 0
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))
    for i in range(number_of_items):
        price = float(input("Price of item: "))
        total += price
    print(f"Total price for {str(number_of_items)} items is ${total}")


main()
