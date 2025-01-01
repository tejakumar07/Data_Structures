def unionOfTwoArrays(arr1,arr2):
    n,m = len(arr1),len(arr2)
    i,j = 0,0
    union = []
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
    while i < n:
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
    while j < m:
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1
    return union
def main():
    arr1 = list(map(int,input("ARRAY 1: ").split()))
    arr2 = list(map(int,input("ARRAY 2: ").split()))
    print(f"First ARRAY 1: {arr1}")
    print(f"Second ARRAY 2: {arr2}")
    arr1.sort()
    arr2.sort()
    print(f"The Union Of Arrays: {unionOfTwoArrays(arr1,arr2)}")
if __name__ == "__main__":
    main()
