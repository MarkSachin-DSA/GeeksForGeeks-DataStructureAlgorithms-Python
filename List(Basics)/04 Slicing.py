l = [10,20,30,40,50]

# Iterate till the last element with step size as 2.
print(l[0:5:2])

# When base is not specified, it defaults from base.
print(l[:3])

# When an end is not specified, it defaults to end.
print(l[3:])

# Negative step, the end index should be greater than start index
print(l[4:1:-1])

# Negative step, without any range
print(l[::-1])

# To give whole list
l2 = l[:]
print(l2)

