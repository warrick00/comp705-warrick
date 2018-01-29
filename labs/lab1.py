"""
Jon Shallow
UNHM COMP705/805 Lab 1
An Introduction to Python
Jan 19, 2018

The purpose of this file is to learn BASIC python syntax and data structures.
There is an accompanying test file. Place both files in the same directory,
and then run:
$ python tests.py

You will see a print out of tests that are being run, and your result.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""

def give_me_a_string():
    
    return "this is a string"
    
    pass

def give_me_an_integer():
   
    return 17
    
    pass 

def give_me_a_boolean():
    
    return 'good' not in 'this is a great example'

    pass

def give_me_a_float():
    
    return 3.7888899987

    pass

def give_me_a_list():
    
    list = ['blue' , 'green', 'yellow']
    
    return list

    pass

def give_me_a_dictionary():
    
    food = {"apple" : "yes","table" : "no"}

    return food

    pass

def give_me_a_tuple():
    
    tup1 = ('things', 'stuff', 10, 21);

    return tup1

    pass

def sum_numbers_one_to_ten():
    start = 1 
    end = 10 

    numlist = range(start, end + 1)
    finalsum = sum(numlist)
    return finalsum


    pass

def check_is_even(number):
    if number  % 2 == 0:  
     return True
    else:
     return False     

    
    pass

def check_is_less_than(number1, number2):
    """
    This functions returns True if number1 < number2
    else False
    """

    if number1 < number2:
        return True
    
    else:
        return False 
    
    pass
