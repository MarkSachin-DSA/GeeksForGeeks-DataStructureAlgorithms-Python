# I/p: l = [8,100,20,40,3,7] and x = 10
# O/p: [8,3,7] all are lesser than x


# Requirement: Create a function which takes an array and an element as input \
# and returns a list which is smaller than the given element.


def get_smaller_num(test_list,x):
    sample_list = []
    length_of_list = len(test_list)
    for i in range(0, length_of_list):
        if test_list[i] < x:
            sample_list.append((test_list[i]))
    return sample_list


l = [8,100,20,40,3,7]
x = 10
a = get_smaller_num(l,x)
print(a)