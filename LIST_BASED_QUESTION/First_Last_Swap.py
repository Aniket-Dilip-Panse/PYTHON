# Given a list, write a Python program to swap first and last element of the list.
def swap_first_last(my_list):
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
    return my_list

print(swap_first_last([1, 2, 3, 4, 5, 6]))