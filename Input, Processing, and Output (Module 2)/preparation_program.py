# Phillip Shane Ashford COP 1000

# Write a Python program that determines the average of three test scores.
# The program should prompt the user to enter the three scores from the keyboard.
# All test scores are to be entered as scores out of 100 but without the % sign.
# The program should calculate the average as a percent and display it accurate
#   to two decimal places with the % symbol immediately following the final digit.
#   See the sample output below. Upload your completed Python program to this
#   dropbox.  As with all assessments and assignments, your programs should:
#
# Start with a comment that includes your name and course number.
# Include pseudocode that describes all steps required to solve the problem.
# Employ variable names that describe the values they store and adhere to Python
#    naming conventions.
# Include additional comments as needed to annotate your code.
# Use correct spelling and grammar.
# Use f-strings for outputs.
# SAMPLE OUTPUT
# Enter the score for test 1 95
# Enter the score for test 2 80
# Enter the score for test 3 85
# The average of these scores is 86.67%.

############################################

# Phillip Shane Ashford COP 1000
#Pseudocode:
#   Input score from each test and store in unique variables.
#   Store quotient of the sum of the three test variables divided by 3 in
#       variable.
#   Print an f-string that concatenates 'The average of these scores is' plus
#       the formatted value of the average score variable placeholder plus
#       '%.'

def main():
    score_1 = float(input('Enter the first test score: '))
    score_2 = float(input('Enter the second test score: '))
    score_3 = float(input('Enter the third test score: '))

    average_score = (score_1 + score_2 + score_3)/3

    print(f'The average of these scores is {average_score:.2f}%.')

    main()
