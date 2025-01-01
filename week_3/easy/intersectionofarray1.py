def intersectionOfArray(arr1,arr2):
    intersection = []
    n,m = len(arr1),len(arr2)
    i,j = 0,0
    while i < n and j < m:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            if len(intersection) == 0 and intersection[-1] != arr1[i]:
                intersection.append(arr1[i])
            i += 1
            j += 1
    return intersection
def main():
    arr1 = list(map(int,input("ARRAY 1: ").split()))
    arr2 = list(map(int,input("ARRAY 2: ").split()))
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    arr1.sort()
    arr2.sort()
    print(f"Intersection of Both Arrays are: {intersectionOfArray(arr1,arr2)}")

if __name__ == "__main__":
    main()