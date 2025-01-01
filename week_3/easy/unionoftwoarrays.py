# This is the union of two sorted arrays
arr = [1,2,3,4,5,6,6,7,8,8,10]
arr1 = [1,2,3,4,9,9,9,11]
union = set()
for i in arr:
    union.add(i)
for i in arr1:
    union.add(i)
print(list(union))


'''
arr = [1, 2, 3, 4, 5, 6, 1, 2, 3, 3]
arr1 = [1, 2, 3, 4, 9, 0, 6, 7]

union = set(arr) | set(arr1) # ~ union = set(arr).union(set(arr1))

print(union)
'''