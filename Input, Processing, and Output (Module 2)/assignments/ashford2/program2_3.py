# Phillip Shane Ashford 2510522

# ASSIGNMENT
# A taxable item is available in multiple quantities. Write a program that prompts the user for the unit price of the item and the number being purchased. The sales tax rate is 7%. Store that to properly named constant  as a decimal. Calculate and print the subtotal, the sales tax, and the total amount due. Display commas for numbers of 1,000 or more. Note the apostrophe in item's in the Example Output below. Your prompt should do that, too.
# Example Output
# Enter the item's unit price 749.99
# Enter the quantity 2
# The subtotal is $1,499.98
# Sales tax is $105.00
# Total due is $1,604.98
########

# Pseudocode
# Store tax rate
# Input unit price
# Input quantity of item
# Calculate subtotal
# Calculate sales tax
# Calculate total amount due
# Print subtotal, sales tax, and total amount due

def main():
    # Store tax rate in constant
    TAX_RATE = 0.07

    # Prompt for unit price
    unit_price = float(input('Enter unit price '))

    # Calculate mixed number integer from numerator and denominator. (This is a floating number because certain units may be purchaseable in partial quantities (ie 2.5 lb walnuts))
    item_quantity = float(input('Enter item quantity '))

    # Assign subtotal by calculating product of unit price and quantity
    subtotal = unit_price * item_quantity

    # Assign sales tax by calculating product of subtotal and tax rate
    sales_tax = subtotal * tax_rate

    #Assign total by calculating sum of subtotal and sales tax
    total = subtotal + sales_tax

    #Print subtotal, sales tax, and total
    print(f'Your subtotal is ${subtotal:,.2f}')
    print(f'Your sales tax is ${sales_tax:,.2f}')
    print(f'Your total due is ${total:,.2f}')

    main()
