# Phillip Shane Ashford 2510522

# Write a program that prompts an SPC grad to enter her hourly pay rate and hours worked last week. Both values may not be integers. Understanding that "time and a half" applies to hours in excess of forty, calculate and print the grad's regular pay, overtime pay, and total pay for the week. Outputs should display currency format with $ signs, two decimals, and commas for thousands.

########

# Pseudocode
# Prompt for pay rate and assign to variable (float only)
# Prompt for hours worked and assign to variable (float only)
# Calculate overtime pay (if hours worked > than 40 then hours worked - 40 = overtime pay) and assign to variable
# Calculate regular pay (pay rate * hours worked)
# Calculate overtime pay ((pay rate * 1.5) * overtime hours worked)
# Calculate total pay (regular pay + overtime pay)
# Print regular pay
# Print overtime pay
# Print total pay

# Prompt for pay rate and assign to variable (float only)
pay_rate = float(input('What is your hourly pay rate? '))

# Prompt for hours worked and assign to variable (float only)
hours_worked = float(input('How many hours did you work last week? '))

# Calculate overtime pay (if hours worked > than 40, hours worked - 40 = overtime pay) and assign to variable
if hours_worked > 40:
    overtime_hours = hours_worked - 40
else:
    overtime_hours = 0

# Calculate regular pay (pay rate * hours worked)
regular_pay = pay_rate * (hours_worked - overtime_hours)

# Calculate overtime pay (pay rate * overtime hours worked)
overtime_pay = (pay_rate * 1.5) * overtime_hours

# Calculate total pay (regular pay + overtime pay)
total_pay = regular_pay + overtime_pay

# Print regular pay
print(f'Your regular pay is ${regular_pay:,.2f}')

# Print overtime pay
print(f'Your overtime pay is ${overtime_pay:,.2f}')

# Print total pay
print(f'Your total pay is ${total_pay:,.2f}')
