# Requirements
#
# Two programs are required. In each program:
#
# Start with a comment that includes your name and course number.
# Include pseudocode that describes all steps required to solve the problem.
# Employ variable names that describe the values they store and adhere to Python naming conventions.
# Include additional comments as needed to annotate your code.
# Use correct spelling and grammar.
# Use f_strings to output variable values.
# Use the "dunders test" for __name__ equals __main__
# 1. Write a program that contains a main function and a custom, void function named show_larger that takes two random integers as parameters. This function should display which integer is larger and by how much. The difference must be expressed as a positive number if the random integers differ. If the random integers are the same, show_larger should handle that, too. See example outputs. In the main function, generate two random integers both in the range from 1 to 5 inclusive, and call show_larger with the integers as arguments.
# EXAMPLE OUTPUT 1
# 3 is larger than 1 by 2
# EXAMPLE OUTPUT 2
# The integers are equal, both are 3
#
# 2. Write a Python program that can convert a Fahrenheit temperature to Celsius, or vice versa. The program should use two custom functions, f_to_c and c_to_f,  to perform the conversions. Both of these functions should be defined in a custom module named temps. Custom function c_to_f should be a void function defined to take a Celsius temperature as a parameter. It should calculate and print the equivalent Fahrenheit temperature accurate to three decimal places. Custom function f_to_c should be a value-returning function defined to take a Fahrenheit temperature as a parameter. This function should calculate the equivalent Celsius temperature and return it. In the main function, your program should:
#
# prompt the user to enter a temperature as an integer.
# indicate the temperature scale of the temperature just entered.
# call the appropriate function from the temps module.
# Use an f-string to display the equivalent temperature accurate to one decimal place.
# EXAMPLE OUTPUT 1
# Enter a temperature 32
# Was that input Fahrenheit or Celsius c/f? f
# 32 Fahrenheit equals 0.0 Celsius
#
# EXAMPLE OUTPUT 2
# Enter a temperature 100
# Was that input Fahrenheit or Celsius c/f? c
# 100 Celsius is 212.0 Fahrenheit
#
# Put both programs and temps.py in one folder. Zip and upload this folder to earn GRADE POINTS.
