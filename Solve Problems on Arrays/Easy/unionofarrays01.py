# Better Approach

def UnionOfElements(arr1, arr2):
    union_elements = []
    for num in arr1:
        if num not in union_elements:
            union_elements.append(num)
    for num in arr2:
        if num not in union_elements:
            union_elements.append(num)
    return union_elements

if __name__ == "__main__":
    arr1 = [x for x in map(int, input("Array 1: ").split())]
    arr2 = [x for x in map(int, input("Array 2: ").split())]
    print(f"The Array 1 Elements are {arr1}")
    print(f"The Array 2 Elements are {arr2}")
    print(UnionOfElements(arr1, arr2))

