# Phillip Ashford 2510522 COP 1000
#
# Assignment Requirements
#
# 2. In the main function, your program should: prompt the user to enter a temperature as an integer.
# indicate the temperature scale of the temperature just entered.
#
##########################
#
# Pseudocode
# Import 'temps' module
# Define main function
    # Gather input (temperature) from user and assign to temperature variable
    # Gather input (temperature scale) from user and assign to scale variable ('c' or 'f')
    # Write if statement to test if the scale variable is equal to 'c'
        # If so pass the temperature variable as an argument to the c_to_f function in the temps module
    # Write elif statement to test if the scale variable is equal to 'f'
        # If so pass the temperature variable as an argument to the f_to_c function in the temps module and store in a variable named 'celsius'
        # Report the temperature in the celsius variable to the user
    # Otherwise tell user to enter 'c' or 'f'
#
#################################
#
# Import 'temps' module
import temps
# Define main function
def main():
    # Gather input (temperature) from user and assign to temperature variable
    temperature = int(input('Enter a temperature '))
    # Gather input (temperature scale) from user and assign to scale variable ('c' or 'f')
    scale = input('Was that input Fahrenheit or Celsius c/f? ')
    # Write if statement to test if the scale variable is equal to 'c'
    if scale == 'c':
        # If so pass the temperature variable as an argument to the c_to_f function in the temps module
        temps.c_to_f(temperature)
    # Write if statement to test if the scale variable is equal to 'f'
    elif scale == 'f':
        # If so pass the temperature variable as an argument to the f_to_c function in the temps module and store in a variable named 'celsius'
        celsius = temps.f_to_c(temperature)
        # Report the temperature in celsius to the user
        print(f'{temperature} Fahrenheit equals {celsius:.1f} Celsius')
    # Otherwise tell user to enter 'c' or 'f'
    else:
        print('Please enter c or f')

# call the appropriate function from the temps module.
# Use an f-string to display the equivalent temperature accurate to one decimal place.




# Call the main function ONLY if the file is being run as
# a standalone program.
if __name__ == '__main__':
    main()
