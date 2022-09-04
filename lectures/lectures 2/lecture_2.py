print("lecture 2")

# Functions

def F2C(f):
    c = (f - 32.0) * (5.0 / 9.0)
    return c

c1 = F2C(10)
c2 = F2C(50)
c3 = F2C(100)


# Basics and Syntax

# def cook_pizza(type):
    # Do stuff
    # Inside of here


def print_name(name):
    print("My name is", name)

print_name("Andrew")


def double(x):
    return 2 * x

print(double(3))

# Activity

# 1. def get_letter_grade(num_grade):

# 2. calc_calories(21)

# 3. False

# 4. 43 21


# Scope

daily_calcs = 2300
soda_cals = 200

def drink_soda(cals_left):
    return cals_left - soda_cals

daily_calcs = drink_soda(daily_calcs)



# activity

import random

player_name = 'Gandalf'
player_type = 'Wizard'

def roll():
    number = random.randint(1, 20)
    return number


print('A troll attacks')
troll_roll = roll()
player_roll = roll()

print(f'Player: {str(player_roll)}    Troll: {str(troll_roll)}')

'''
1. player_name
    global

2. roll
    global

3. number
    local

4. str
    built-in
'''