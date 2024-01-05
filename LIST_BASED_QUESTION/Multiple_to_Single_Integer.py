#Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350

def multiple_to_single_integer(my_list):
    return int("".join(map(str,my_list)))
print(multiple_to_single_integer([11, 33, 50]))

def multiple_to_single(my_list):
    empty = ''
    for value in my_list:
        empty += str(value)
    return int(empty)
print(multiple_to_single([11, 33, 50]))