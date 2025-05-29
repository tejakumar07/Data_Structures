# Brute Force Approach

def IntersectionOfTwoArrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    visted = [0] * n2
    intersection = []
    for i in range(n1):
        for j in range(n2):
            if arr1[i] == arr2[j] and visted[j] == 0:
                intersection.append(arr1[i])
                visted[j] = 1
                break
    return f"The Intersection of two arrays are {intersection} "

if __name__ == "__main__":
    arr1 = [x for x in map(int, input("Array1: ").split())]
    arr2 = [x for x in map(int, input("Array2: ").split())]
    print(f"The Entered Array is: {arr1} ")
    print(f"The Entered Array is: {arr2} ")
    print(IntersectionOfTwoArrays(arr1, arr2))

