# program to print list of duplicate from list of integer
import time
print(" ")
def duplicate(my_list):
    my_list_no_duplicate = []
    my_list_duplicate = []
    for value in my_list:
        if value not in my_list_no_duplicate:
            my_list_no_duplicate.append(value)
        elif value in my_list_no_duplicate:
            my_list_duplicate.append(value)
        else:
            pass
    print("original list: ",my_list)
    print(" ")
    print("new list with no duplicate: ",my_list_no_duplicate)
    print(" ")
    print("new list with all duplicate: ",list(set(my_list_duplicate)))
    print(" ")
duplicate([2,4,4,32,4,23,1,3,5,45,6,7,5,36,47,6,63,636,36,33,3,7,8,896,55,6,8,858,36])

print(" ")
print(" ")
# using counter function from collection module
from collections import *
l1 = [2,4,4,32,4,23,1,3,5,45,6,7,5,36,47,6,63,636,36,33,3,7,8,896,55,6,8,858,36]
d = Counter(l1)
print(d)

new_list = list([item for item in d if d[item]>1])
print(new_list)

print(" ")
print(" ")
# using count() method
l1 = [2,4,4,32,4,23,1,3,5,45,6,7,5,36,47,6,63,636,36,33,3,7,8,896,55,6,8,858,36]
new = []
for a in l1:
    n = l1.count(a)
    if n>1:
        if new.count(a)==0:
            new.append(a)
print("Using Count(): ",new)