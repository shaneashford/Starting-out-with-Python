# Phillip Ashford 2510522 COP 1000
#
# Assignment Requirements
#
# Pseudocode
#
# 1. Write a program that contains a main function and a custom, void function named show_larger that takes two random integers as parameters. This function should display which integer is larger and by how much. The difference must be expressed as a positive number if the random integers differ. If the random integers are the same, show_larger should handle that, too. See example outputs. In the main function, generate two random integers both in the range from 1 to 5 inclusive, and call show_larger with the integers as arguments.

import random
# Define main function
def main():
    # Assign 2 random numbers (between 1 and up to and including 5) to two unique variable
    num1 = random.randint (1, 5)
    num2 = random.randint (1, 5)
    # Pass random number variables as arguments to show_larger function
    show_larger(num1, num2)
# Define show_larger function and assign unique parameters to accept arguments
def show_larger(ran1, ran2):
    # Create conditional if statement to test whether the first randomly generated number is greater than AND not equal to the 2nd randomly generated number
    if ran1 > ran2 and ran1 != ran2:
        # Assign difference between the two numbers to a variable
        difference = ran1 - ran2
        # Print a statement to the user indicating that the first number is larger, and indicating the difference between the two numbers
        print(f'{ran1} is larger than {ran2} by {difference}.')
    # Test whether the first randomly generated number is greater than AND not equal to the 2nd randomly generated number
    elif ran2 > ran1 and ran1 != ran2:
        # Assign difference between the two numbers to a variable
        difference = ran2 - ran1
        # Print a statement to the user indicating that the second number is larger, and indicating the difference between the two numbers
        print(f'{ran2} is larger than {ran1} by {difference}.')
    # Otherwise the numbers are the same
    else:
        # Tell the user that the integers are equal
        print(f'The integers are equal, both are {ran1}')

# Call the main function ONLY if the file is being run as a standalone program.
if __name__ == '__main__':
    # Call the main function
    main()
