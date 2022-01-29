# Phillip Shane Ashford 2510522

# Assignment

# Write a program that operates like a point of sale terminal for the purchase of three items in various quantities. The program should accept the name, unit price, and quantity of each item as keyboard inputs. Note that the prompts for the price and quantity should display the item name. A line should be printed that reflects these inputs and includes the subtotal for each item. The program should finish by printing the total for the three items.

############################

# Pseudocode

# Initialize a counter
# Set the accumulator variable which will store the running total to 0
# Write while loop that specifies sentinel value to exit loop
    # Prompt for input and store in variable
    # Prompt for input and store in variable
    # Prompt for input and store in variable
    # Calculate subtotal (unit price * quantity)
    # Print inputs and subtotal for each item
    # Update the accumulator with each iteration (accumulator + subtotal)
    # Advance the counter
# Print the total for all items to the user

#######################################

# Initialize a counter
counter = 0

# Set the accumulator variable which will store the running total to 0
total = 0

# Write while loop that specifies sentinel value to exit loop
while counter < 3:

    # Prompt for input and store in variable
    name = input('Enter the name of your item ')
    # Prompt for input and store in variable
    unit_price = float(input(f'Enter the unit price of your item \"' f'{name}'f'\" '))
    # Prompt for input and store in variable
    quantity = float(input(f'Enter the quantity of your item \"' f'{name}'f'\" '))

    # Calculate subtotal (unit price * quantity)
    subtotal = unit_price * quantity

    # Print inputs and subtotal for each item
    print(f'{int(quantity)} of your item "{name}" priced at {unit_price:,.2f} each yields a subtotal of {unit_price * quantity:,.2f}.')

    # Update the accumulator with each iteration (accumulator + subtotal)
    total = total + subtotal

    # Advance the counter
    counter += 1

# Print the total for all items to the user
print(f'The total for your three items is ${total}')
