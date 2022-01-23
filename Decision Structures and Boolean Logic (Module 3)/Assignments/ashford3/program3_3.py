# Phillip Shane Ashford 2510522

# Write a program that prompts the user to enter a two-digit integer. If the user's input is acceptable, prompt the user to enter another, DIFFERENT two-digit integer. If this input is also acceptable, the program should determine which integer is larger, and by how much, and print the result (see example outputs). If either input is unacceptable, the program should respond with a statement identifying the bad input. Use nested decision blocks and pay close attention to proper indentation.
########

# Pseudocode
# Prompt for a 2 digit integer
# Determine if the input is a 2 digit integer or not (> 9 AND < 100)
    # If the input is a 2 digit integer, prompt for a different 2 digit integer
        # Check if the second integer is a 2 digit integer unequal to the first integer (> 9 AND < 100 AND != the first integer)
            # Determine if the first integer is greater than the second integer
                # If true determine how much larger (1st inetger - 2nd integer)
                # Print larger number and differnce
                # If not determine how much larger the 2nd integer is (2nd integer - 1st integer)
                # Print larger number and differnce
        # Else if the numbers are equal respond with a statement identifying the bad input
        # Else respond with a statement identifying the bad input
# Otherwise respond with a statement identifying the bad input

# Prompt for a 2 digit integer
first_num = int(input('Enter a 2 digit integer '))

# Determine if the input is a 2 digit integer (> 9 AND < 100)
if first_num > 9 and first_num < 100:
# If the input is a 2 digit integer prompt for a different 2 digit integer
    second_num = int(input('Enter a different 2 digit integer '))
# Check if the second integer is a 2 digit integer unequal to the first integer ( > 9 AND < 100 AND != the first integer)
    if second_num > 9 and second_num < 100 and first_num != second_num:
        # Determine if the first integer is greater than the second integer
        if first_num - second_num >= 0:
        # If true determine how much larger (1st inetger - 2nd integer)
            difference = first_num - second_num
            print(f'{first_num} is larger than {second_num} by {difference}.')
        # If not determine how much larger the 2nd integer is (2nd integer - 1st integer)
        else:
            difference = second_num - first_num
            print(f'{second_num} is larger than {first_num} by {difference}.')
    elif first_num == second_num:
        print('This is the same number as your first number.')
    else:
        print('This is not a two digit integer')

# Otherwise respond with a statement identifying the bad input
else:
    print('This is not a two digit integer')
