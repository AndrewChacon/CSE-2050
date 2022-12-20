
# CODING QUESTION 1
print("Coding Question 1")
print("Please enter a number to check if it is a leap year or not")

year = int(input("Input: "))
is_a_leap_year = False

'''
A leap year is exactly divisible by 4 = true
if the year is not divisible by 100 = true
if the year is divisible by 400 = true

else = false
'''

if(year % 400 == 0) or year % 100 != 0 and year % 4 == 0:
    is_a_leap_year = True
else:
    is_a_leap_year = False

print("Output: {}".format(is_a_leap_year))




# CODING QUESTION 2

print("Coding Question 2")
print("Enter a number and see how many digits are in it")

number = int(input("Input: "))
num_of_digits = 0

# turn input into string then array and return the length

num_of_digits = len(str(number))

print("Output: {}".format(num_of_digits))