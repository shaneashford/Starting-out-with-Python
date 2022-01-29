# Phillip Shane Ashford 2510522

#################################
# Pseudocode

# Initialize variable to hold range value
# Initialize counter to control and exit while loop when complete
# Write while loop that tracks the value of the counter
    # Write for loop with range function assigned to variable
        # Print output
    # Print to new line after each iteration of the for loop
    # Reduce the value in the range variable by 1 (range -= 1) for the next loop iteration
    # Reduce the counter by 1 for the next loop iteration

#################################

# Initialize variable to hold range value
range_value = 10

# Initialize counter to control and exit while loop when complete
counter = 9

# Write while loop that tracks the value of the counter
while counter < 10 and counter > -1:
    # Write for loop with range function assigned to variable
    for num in range(range_value):
        # Print output
        print(num, end='')
    # Print to new line for desired output
    print()

    # Reduce the value in the range variable by 1 for the next loop iteration
    range_value -= 1

    # Reduce the counter by 1 for the next loop iteration
    counter -= 1
