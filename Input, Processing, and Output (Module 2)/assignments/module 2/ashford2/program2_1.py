# Phillip Shane Ashford 2510522

# ASSIGNMENT
# Write a program that converts miles to kilometers. Look up the conversion
#   factor and assign it to a properly named constant (see page 80). The
#   program should permit the user to enter the miles perhaps with decimals,
#   from the keyboard. Print the result showing both distances using an
#   f_string with the kilometers accurate to three decimal places.
# Required Output
# Enter the miles 12.75
# 12.75 miles is 20.519 kilometers
########

# Pseudocode
# Store conversion factor as constant
# Input miles
# Convert to kilometers
# Print both miles and kilometers

def main():
    #Store miles to kilometers conversion factor (1 mi = 1.60934 km)
    CONVERSION_FACTOR = 1.60934

    # Prompt input from user and store in variable
    miles = float(input('Enter miles '))

    # Assign product of miles and conversion factor in kilometers variable
    kilometers = miles * CONVERSION_FACTOR

    # Print conversion
    print(f'{miles} miles is equal to 'f'{kilometers:.3f} kilometers.')

    main()
