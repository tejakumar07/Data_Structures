arr1 = [1,1,2,3,4,4,5]
arr2 = [1,1,2,3,3,4,4,5,6]

union = set(arr1) & set(arr2)
print(list(union))