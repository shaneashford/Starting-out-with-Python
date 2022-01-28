# Phillip Shane Ashford COP 1000

# ASSIGNMENT REQUIREMENTS
# 1. Write a Python program that uses a for loop with the range function to process the integers from 5 to 50 in increments of 5. See page 182 to learn how to do this with the range function. The loop should also print the square and cube of each integer in a table. The integers column should be centered and 7 characters wide, the squares column should be right-aligned and 8 characters wide, and the cubes column should be right-aligned and 12 characters wide. Use an f-string and refer back to pages 70-78 to review formatting. Include column headings with the same alignments and display commas for numbers of 1000 or more. See required output.

############################################

# Pseudocode:

# Print 'integer' column heading in a column centered and 7 characters wide, 'squares' column heading right aligned and 8 characters wide, and 'cubes' column heading right aligned and 12 characters wide
# Write for loop with range function from 5 to 51 with step value of 5
    # Print the targeted variable in a column centered and 7 characters wide
    # Print the square of the targeted variable right aligned and 8 characters wide
    # Print the cube of the targeted variable right aligned and 12 characters wide

############################################

# Print 'integer' column heading in a column centered and 7 characters wide, 'squares' column heading right aligned and 8 characters wide, and 'cubes' column heading right aligned and 12 characters wide
print(f'{"integer":^7}{"squares":>8}{"cubes":>12}')

# Write for loop with range function from 5 to 51 with step value of 5
for num in range(5, 51, 5):
    # Print the targeted variable in a column centered and 7 characters wide
        print(f'{num:^7,}', end = '')
    # Print the square of the targeted variable right aligned and 8 characters wide
        print(f'{num ** 2:>8,}', end = '')
    # Print the cube of the targeted variable right aligned and 12 characters wide
        print(f'{num ** 3:>12,}')
