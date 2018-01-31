"""
lab2.py
Ryan Warrick
1/30/2018
"""

def squared(num_list):
    """
    squares numbers in num_list
    num_list: list of numbers
    Returns: list of these numbers squared
    """
    new_list = [] # initialize lise to hold result
    #iterate through each num_list and aquare each element
    for num in num_list:
        sq_num = pow(num,2) #num **2
        new_list.append(sq_num)
    return new_list

def check_title(title_list):
    """
    Removes strings in the title_list that have numbers and
    aren't title case
    title_list: list of strings
    Returns: list of strings that are title_list
    """
    for num in title_list:
        title_list.remove(numbers)
        title_list.remove()
        new_title_list.append()
    return new_title_list

def restock_inventory(inventory):
    """
    increase inventory of each item in dictionary by 10
    inventory: a dictionary with:
    """
