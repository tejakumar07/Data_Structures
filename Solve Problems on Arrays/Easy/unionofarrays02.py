# Optimal Approach
# Using two pointer approach

def UnionOfArrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    i = 0
    j = 0
    union = []
    while (i < n1 and j < n2):
        if arr1[i] <= arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
        else:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j+=1
    while i < n1:
        if len(union) == 0 or union[-1] != arr1[i]:
            union.append(arr1[i])
        i+=1
    while j < n2:
        if len(union) == 0 or union[-1] != arr2[j]:
            union.append(arr2[j])
        j+=1
    return f"The Union of two arrays is {union} "

if __name__ == "__main__":
    arr1 = [x for x in map(int, input("Array 1: ").split())]
    arr2 = [x for x in map(int, input("Array 2: ").split())]
    print(f"The 1st array is {arr1} ")
    print(f"The 2nd arrays is {arr2} ")
    print(UnionOfArrays(arr1, arr2))

