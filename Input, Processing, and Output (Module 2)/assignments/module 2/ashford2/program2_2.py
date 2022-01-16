# Phillip Shane Ashford 2510522

# ASSIGNMENT
# Write a program that prompts the user to enter both the numerator and
#   denominator of an improper fraction. Review the Python math operators on
#   page 54 and use an f_string to express the improper fraction as a mixed
#   number.
# Example Output
# Enter the numerator 34
# Enter the denominator 7
# As a mixed number that is 4 and 6/7
########

# Pseudocode
# Prompt input for numerator
# Prompt input for denominator
# Convert improper fraction to mixed number
# Print mixed number

def main():
    # Prompt for numerator and store in variable
    numerator = int(input('Enter numerator '))

    # Prompt for denominator and store in variable
    denominator = int(input('Enter denominator '))

    # Calculate mixed number integer from numerator and denominator
    mixed_number_integer = numerator//denominator

    # Calculate mixed number remainder from numerator and denominator
    mixed_number_remainder = numerator % denominator

    # Print  mixed number integer and mixed number remainder and store in
    #   variable.
    print(f'As a mixed number that is {mixed_number_integer} and {mixed_number_remainder}/{denominator}')

    main()
