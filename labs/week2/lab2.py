"""
lab3.py
Ryan Warrick
2/6/2018
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
        key: string that is the name of the inventory item
        value: integer that equals the number of that item is restocked
    Returns: updated dictionary where each inventory item is restocked
    """
def filter_0_items(inventory):
    """
    Removes items that have a value of 0 from a dictionary of inventories
    inventory: dictionary with:
        key: trinf that is the name of the inventory item
        value: nteger that equals the number of that item currenlty on hand
    Returns: the same inventory_dict with and item that had 0 quantitiy removed
    """
def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
        grades: a dictionary of grades with"
        key: string of students name
        value: list of integer grades recieved in class
        Returns: dictionary that averages out the grades of each students
    """
