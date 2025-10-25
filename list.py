a = [1,2,3,4,5,10,11]
b = [2,3,1,0,5]

b_set = set(b)
result = [x for x in a if x not in b_set]

print(*result)
