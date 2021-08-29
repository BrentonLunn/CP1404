"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    print_subject_details(data)


def print_subject_details(data):
    """Read subject data and print it neat"""
    for line in data:
        print(f"{line[0]} is taught by {line[1]:12} and has {str(line[2]):3} students")


def get_data():
    subject_data = []
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_data.append(parts) # add parts to a list
    input_file.close()
    return subject_data

main()