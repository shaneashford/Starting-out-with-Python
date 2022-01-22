# Phillip Shane Ashford COP 1000

# ASSIGNMENT REQUIREMENTS
# Write a Python program for an online MoonBucks coffee order. Coffee is sold by the pound, and the price per pound depends upon the quantity ordered according to the table shown below. Partial pounds are not sold. Shipping is $1.00 per pound, but free for coffee orders over $150 before tax. The user must enter the number of pounds desired from the keyboard. The program will then display the cost of the coffee, the 7% sales tax, shipping charges (if any) and the total amount due. All four values should be displayed in currency format with the $ sign right up against the first digit. See SAMPLE OUTPUTS below.
# MoonBucks Coffee Company - Coffee Prices
# 40 pounds or more          $7.50 per lb.
# 20 pounds or more          $8.75 per lb.
# 10 pounds or more          $10.00 per lb.
# 1 to 9 pounds              $12.00 per lb.
#
# Start with a comment that includes your name and course number.
# Include pseudocode that describes all steps required to solve the problem.
# Employ variable names that describe the values they store and adhere to Python naming conventions.
# Include additional comments as needed to annotate your code.
# Use correct spelling and grammar.
# Use f-strings for all outputs.
# SAMPLE OUTPUT
# How many pounds are you ordering? 15
# Cost of coffee $150.00
# 7% sales tax $10.50
# Shipping fee $15.00
# Total payable $175.50
#
# SAMPLE OUTPUT
# How many pounds are you ordering? 50
# Cost of coffee $375.00
# 7% sales tax $26.25
# Shipping fee $0.00
# Total payable $401.25

############################################

# Phillip Shane Ashford COP 1000

#Pseudocode:
# Assign tax rate to constant
# Assign free shipping threshold to constant
# Assign tier pricing to constants
# Prompt for quantity of Coffee (test for integer)
# Determine pricing tier with if-else design structure
# Calculate subtotal and assign to a variable
# Calculate tax total and assign to a variable
# Determine free shipping status and assign to variable
# Assign shipping fee to a variable
# Calculate total payable and assign to a variable
# Print subtotal
# Print sales tax
# Print shipping fee
# Print total payable

# Assign tax rate to constant
TAX_RATE = 0.07

# Assign free shipping threshold to constant
FREE_SHIPPING_THRESHOLD = 150

# Assign tier pricing to contants
TIER_4 = 7.50
TIER_3 = 8.75
TIER_2 = 10.00
TIER_1 = 12.00

# Prompt for quantity of Coffee (test for integer) and assign to variable
coffee_quantity = int(input('How many pounds of coffee would you like to order? '))

# Determine pricing tier with if-else design structure
if coffee_quantity < 10 and  coffee_quantity > 0:
    tier = TIER_1
elif coffee_quantity >= 40:
    tier = TIER_4
elif coffee_quantity >= 20:
    tier = TIER_3
else:
    tier = TIER_2

# Calculate subtotal and assign to a variable
subtotal = tier * coffee_quantity

# Calculate tax total and assign to a variable
tax_total = subtotal * TAX_RATE

# Determine free shipping status and assign to variable
if subtotal >= FREE_SHIPPING_THRESHOLD:
    free_shipping_eligible = True
else:
    free_shipping_eligible = False

# Determine shipping fee and assign to variable
if free_shipping_eligible == True:
    shipping_fee = float(0)
else:
    shipping_fee = float(coffee_quantity)

# Calculate total payable and assign to a variable
total = subtotal + tax_total + shipping_fee

# Print subtotal
print(f'Your subtotal is ${subtotal:,.2f}')

# Print sales tax total
print(f'Your sales tax is ${tax_total:,.2f}')

# Print shipping fee
print(f'Your shipping fee is ${shipping_fee:,.2f}')

# Print total payable
print(f'Your total is ${total:,.2f}')
