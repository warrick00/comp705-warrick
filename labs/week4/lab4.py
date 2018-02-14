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

    >>> squared([1,2,3])
    [1, 4, 9]
    >>> squared([])
    []
    >>> squared ([-1, -2])
    [1, 4]
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

    >>> check_title(['Hello World', 'Hello_world','Title']),
    [('Hello World', 'Title')]

    """
    new_list = []
    for title in title_list:
        if title.istitle() and title.isalpha():
            new_list.append(title)
    return new_list


def restock_inventory(inventory):
    """
    increase inventory of each item in dictionary by 10
    inventory: a dictionary with:
        key: string that is the name of the inventory item
        value: integer that equals the number of that item is restocked
    Returns: updated dictionary where each inventory item is restocked
    item assignmnet on dictionary yes
        because mutable
    """
    new_inventory = {}
    for key, val in inventory:
        val = val +10
        new_inventory[key] = val
    return new_inventory

def filter_0_items(inventory):
    """
    Removes items that have a value of 0 from a dictionary of inventories
    inventory: dictionary with:
        key: trinf that is the name of the inventory item
        value: nteger that equals the number of that item currenlty on hand
    Returns: the same inventory_dict with and item that had 0 quantitiy removed
    """
    new_inventory = {}
    for k , v in inventory.items():
        if v != 0:
            new_inventory[k] = v
    return new_inventory

def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
        grades: a dictionary of grades with"
        key: string of students name
        value: list of integer grades recieved in class
        Returns: dictionary that averages out the grades of each students
    """
    new_grades = {}
    for student_name, student_grades in grades.items():
        new_grades[student_name] = sum(student_grades) / len(student_grades)
    return new_grades

if __name__ == '__main__':
    import doctest
    doctest.testmod()
