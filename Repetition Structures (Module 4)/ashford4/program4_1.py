# Phillip Shane Ashford 2510522

# ASSIGNMENT
# Write a program that uses a while loop to generate a table showing the 7% sales tax and total charge for subtotals from $0.20 to $5.00 in $0.20 intervals (see required output). Dollar signs are not required. Use a properly named constant for the tax rate. The values in all three columns should be centered in columns 9 characters wide. Include underlined headings centered over each column as shown.

#############################

# Pseudocode

# Assign tax rate to constant
# Assign start, stop, and step value for range function to constants
# Specify starting value of setinel variable
# Assign start, stop, and step constants to float-to-integer-conversion constants to feed the non-floating-pont-number-supporting range function
# Write while loop that specifies sentinel value to exit loop
    # Print 'sales tax', 'subtotals', and 'totals' column headings in columns centered and 9 characters wide each
    # Print underlined headings
    # Write for loop with range function
        # Print subtotal in a column centered and 9 characters wide
        # Print sales tax in a column centered and 9 characters wide
        # Print total in a column centered and 9 characters wide
    # Adjust sentinel value after for loop runs once

##########################

# Assign tax rate to constant
TAX_RATE = .07

# Assign start, stop, and step value for range function to constants
START_VALUE = 0.2
STOP_VALUE = 5.01
STEP_VALUE = 0.2

# Specify starting value of setinel variable
run = False

# Assign start, stop, and step constants to float-to-integer-conversion constants to feed the non-floating-pont-number-supporting range function
START_VALUE_TO_INT = int(START_VALUE * 100)
STOP_VALUE_TO_INT = int(STOP_VALUE * 100)
STEP_VALUE_TO_INT = int(STEP_VALUE * 100)

# Write while loop that specifies sentinel value to exit loop
while run == False:
    # Print 'sales tax', 'subtotals', and 'totals' column headings in columns centered and 9 characters wide each
    print(f'{"subtotal":^9}{"sales tax":^9}{"total":^9}')
    # Print underlined headings
    underline = '------'
    print(f'{underline:^9}{underline:^9}{underline:^9}')

    # Write for loop with range function
    for num in range(START_VALUE_TO_INT, STOP_VALUE_TO_INT, STEP_VALUE_TO_INT):
        # Print subtotal in a column centered and 9 characters wide
            print(f'{float(num/100):^9.2f}', end = '')
        # Print sales tax in a column centered and 9 characters wide
            print(f'{float(num/100 * TAX_RATE):^9.2f}', end = '')
        # Print total in a column centered and 9 characters wide
            print(f'{float(num/100 + num/100 * TAX_RATE):^9.2f}')
    # Adjust sentinel value after for loop runs once
    run = True
