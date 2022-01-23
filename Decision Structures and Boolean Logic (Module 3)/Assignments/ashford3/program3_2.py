# Phillip Shane Ashford 2510522

# Write a program that prompts the user to enter an odd multiple of 19 that is more than 60 and less than 200. Respond to good inputs with "Good input" and displaying the other factor. Respond to incorrect inputs with "Bad input". Use logical operators and just one if expression (no nested ifs).
########

# Pseudocode
# Prompt for input from user
# Calculate if input meets requirements (if the input / 19 contains no remainder and is > 60 and < 200 it does)
# Print response to input

# Prompt for input from user
num_to_test = int(input('Enter an odd multiple of 19 that is more than 60 and less than 200 '))

# Calculate if input meets requirements (if the input % 2 equals 1 AND the input % 19 contains equals 0 AND the input is > 60 and < 200 it meets the requirements)
if num_to_test % 2 == 1 and num_to_test % 19 == 0 and num_to_test > 60 and num_to_test < 200:
# Print response to user's input
    print(f'Good input. The other factor is {int(num_to_test / 19)}.')
else:
# Print response to user's input
    print('Bad input')
