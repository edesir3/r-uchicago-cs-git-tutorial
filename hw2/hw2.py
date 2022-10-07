"""
CMSC 14100, Autumn 2022
Homework #2

We will be using anonymous grading, so please do NOT include your name
in this file

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URL of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.

"""
from time import time

from numpy import true_divide


def add_one_and_multiply(a, x):
    """ Add 1 to a, then multiply by x"""
    ### EXERCISE 1 -- 

    result = (1 + a) * x

    
    return result


def are_congruent_mod_n(a, b, n):
    """
    Check if a and b are congruent mod n

    Inputs:
        a (int): a value
        b (int): another value
        n (int): the modulus to use

    Returns: True if a and b are congruent mod n, and False otherwise.
    """

    ### EXERCISE 2 -- 

    if a % n == b % n:
        result = True 
    elif a % n != b % n:
        result = False 
    
    
    return result


def find_interest_rate(amount, principal, time):
    """
    Given the amount returned at the end of a time period for
    a bond, the principal or face value of the bond, and the time in years,
    compute the interest rate (using simple interest).

    Inputs:
        amount (float): the payoff amount for the loan
        principal (float): the face value of the bond
        time (float): the number of years the bond was held

    Return (float): the interest rate of the bond
    """
    
    assert amount > 0
    assert principal > 0
    assert time > 0

    ### EXERCISE 3 -- 

    result = ((amount - principal) * 100)/ (principal * time)

    
    return result

#######
# Constants used in Exercises 4-7
#######

URBAN_POPULATION_THRESHOLD = 50000
URBAN_DENSITY_THRESHOLD = 1000

RURAL_POPULATION_THRESHOLD = 2500
RURAL_DENSITY_THRESHOLD = 500

def is_urban_county(population, area):
    """
    Does a county qualify as urban?

    Inputs:
        population (int): the number of people who live in an area
        area (float): the area of the county in square miles

    Returns (boolean): Returns True, if the county qualfies as urban,
        False otherwise.
    """
    
    assert population >= 0
    assert area > 0

    
    ### EXERCISE 4 -- 
    if (population >= URBAN_POPULATION_THRESHOLD and area >= 
    URBAN_DENSITY_THRESHOLD):
        result = True
    if (population >= RURAL_POPULATION_THRESHOLD and area >= 
    RURAL_DENSITY_THRESHOLD):
        result = False
    else:
        result = False

    return result


def is_other_county(population, area):
    """
    Does a county qualify as neither rural nor urban?

    Inputs:
        population (int): the number of people who live in an area
        area (float): the area of the county in square miles

    Limitations: your solution for this task must use
    relational operations and conditional statements.
    You may not use logical operators (and, or, not).

    Returns (boolean): Returns True, if the county qualfies as other,
        False otherwise.

    """
    
    assert population >= 0
    assert area > 0


    ### EXERCISE 5 -- 
    
    if population != URBAN_POPULATION_THRESHOLD: 
        result = True
    if area != URBAN_DENSITY_THRESHOLD:
        result = True
    elif population !=  RURAL_POPULATION_THRESHOLD: 
        result = True
    elif area != RURAL_DENSITY_THRESHOLD:
        result = True
    else: 
        result = False



    return result


def alt_is_other_county(population, area):
    """
    Does a county qualify as neither rural nor urban?

    Inputs:
        population (int): the number of people who live in an area
        area (float): the area of the county in square miles

    Limitations: your solution for this task must use only
    relational operations and logical operators (and, or, not).  You
    may not use conditional expressions or conditional statements for
    this exercise.

    Returns (boolean): Returns True, if the county qualfies as other,
        False otherwise.

    """
    
    assert population >= 0
    assert area > 0

    ### EXERCISE 6 -- 

    result = True == (population < 50000 and area > 2500 or population 
    < 1000 and area > 500)
    result = False == (population < 50000 and area > 2500 or population 
    < 1000 and area > 500)

    
    return result


def label_county(population, area):
    """
    Label an area as rural, urban, or other based on its population
    and population density.

    Inputs:
        population (int): the number of people who live in an area
        area (float): the area of the county in square miles

    Returns (string): "rural", "urban", or "other"
    """
    
    assert population >= 0
    assert area > 0

    result = ("urban", "rural", "other")

    ### EXERCISE 7 -- 
    
    if (population >= URBAN_POPULATION_THRESHOLD and area 
        >= URBAN_DENSITY_THRESHOLD):
        result ("urban")
    elif (population <=  RURAL_POPULATION_THRESHOLD and area <= 
        RURAL_DENSITY_THRESHOLD):
        result ("rural")
    elif (population < URBAN_POPULATION_THRESHOLD or population > 
        RURAL_POPULATION_THRESHOLD and area < URBAN_DENSITY_THRESHOLD or 
        area > RURAL_DENSITY_THRESHOLD):
        result ("other")
        
    
    return result


def compute_fee(length, weight):
    """
    Determine the port fee paid by for a container based on its weight
    and length.  All containers that weigh more than 30000kg must pay a port
    fee of $300.  The fee for containers below this limit is
    determined by their length: 40 ft containers pay $300,
    20 ft containers pay $150, and 10ft containers pay $75.
    """
    
    assert weight > 0
    assert length in [10, 20, 40]

    ### EXERCISE 8 -- 
    if weight > 3000:
        fee = 300
    elif weight < 3000 and length == 40 :
        fee = 300
    elif weight < 3000 and length == 20 :
        fee = 150
    elif weight < 300 and length== 10:
        fee = 75

  
    return fee
