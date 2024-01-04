# Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. 
def swap(my_list, pos1, pos2):
    print(f'Original List: {my_list}')
    my_list[pos1], my_list[pos2] = my_list[pos2], my_list[pos1]
    print(f'Swapped List: {my_list}')
swap([1, 2, 3, 4, 5, 6], 0, 5)