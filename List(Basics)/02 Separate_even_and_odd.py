# I/p = [10,41,20,15,80]
# O/p even = [10,30,80] and odd = [41,15]


# Requirement: given a list separate the list into even and odd and return 2 list.

def separate_list(temp_list):
    odd_list = []
    even_list = []
    length_of_list = len(temp_list)
    for i in range(0, length_of_list):
        if temp_list[i] % 2 == 0:
            even_list.append(temp_list[i])
        else:
            odd_list.append(temp_list[i])
    return odd_list,even_list


temp_list = [10, 41, 20, 15, 80]
a, b = separate_list(temp_list)
print(a)
print(b)

