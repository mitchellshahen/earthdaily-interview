"""
Modules to perform the code review tasks for EarthDaily
"""

# ----- # Fibonacci Numbers Task # ----- #

def fib_no_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_no_iter(n - 1) + fib_no_iter(n - 2)

# ----- # List Merge # ----- #

def list_manip(original_list, add_list, delete_list):
    """
    """

    # add the add list to the original list one element at a time
    for element in add_list:
        if element not in original_list:
            original_list.append(element)

    # delete the elements in the delete list from the above list
    for element in delete_list:
        if element in original_list:
            original_list.remove(element)

    # create a dictionary of keys (string lengths)
    # and values (strings of that length)
    elem_dict = {}
    for element in original_list:
        elem_len = len(element)
        if elem_len not in elem_dict.keys():
            elem_dict[elem_len] = []
        elem_dict[elem_len].append(element)

    # sort each dictionary value list alphabetically in reverse
    for elem_list in elem_dict.values():
        if len(elem_list) > 1:
            elem_list.sort(reverse=True)

    # sort the dictionary keys by number in reverse
    dict_key_list = sorted(list(elem_dict.keys()), reverse=True)

    # unpack the dictionary adding each value list to a final list
    # starting with the longest strings and keeping the order
    # of each value list
    final_list = []
    for key in dict_key_list:
        elem_list = elem_dict[key]
        for element in elem_list:
            final_list.append(element)

    return final_list

# ----- # TESTING EACH MODULE # ----- #

final_number = fib_no_iter(n=10)
print(final_number)

final_list = list_manip(
    original_list=["one", "two", "three"],
    add_list=["one", "two", "five", "six"],
    delete_list=["two", "five"]
)
print(final_list)

