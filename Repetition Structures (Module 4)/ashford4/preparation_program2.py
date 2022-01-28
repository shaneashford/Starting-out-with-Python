# Phillip Shane Ashford COP 1000

# ASSIGNMENT REQUIREMENTS
# 2. Write a Python program that prompts the user to enter an integer and reports whether the input was even or odd. Assume that the user follows instructions and enters only integers. The program must use a while loop and it should continue until the user enters zero. See pages 192-194 to learn about sentinels.
############################################

# Phillip Shane Ashford COP 1000

#Pseudocode:
# Prompt for input and assign to variable
# Write while loop that specifies sentinel value to exit loop
    # Write nested if-else decision structure to test for even and odd numbers and report to user.

############################################
# Prompt for input and assign to variable
num = int(input('Enter an integer '))

# Write while loop that specifies sentinel value to exit loop
while num != 0:
    # Write nested if-else decision structure to test for even and odd numbers and report to user.
    if num % 2 == 0:
        print(f'{num} is an even number.')
        num = int(input('Enter an integer '))
    else:
        print(f'{num} is an odd number.')
        num = int(input('Enter an integer '))
