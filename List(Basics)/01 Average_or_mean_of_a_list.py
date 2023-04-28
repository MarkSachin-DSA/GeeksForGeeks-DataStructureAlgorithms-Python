# I/p l = [30,60,40]
# o/p 43.33

# Requirement: A function which takes list as input and returns an average of the list.

def average_of_list(ex_list):
    length_of_list = len(ex_list)
    sum_of_list = 0
    for i in range(0,length_of_list):
        sum_of_list = sum_of_list + ex_list[i]
    average = sum_of_list/length_of_list
    return average


# Input 1


lis_1 = [10, 20, 30, 40]
op_1 = round(average_of_list(lis_1),2)
lis_2 = [30, 60, 40]
op_2 = round(average_of_list(lis_2),2)
print(op_1,op_2)