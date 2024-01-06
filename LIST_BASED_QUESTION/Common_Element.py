# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
def common_element(list1,list2):
    for i in list1:
        for j in list2:
            if i==j:
                return True
            else:
                pass
print(common_element([1,2,3,4],[4,6,7,8]))