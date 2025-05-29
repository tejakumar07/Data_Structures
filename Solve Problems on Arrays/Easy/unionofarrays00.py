# Brute Force Approach
def UnionOfTwoArrays(arr1, arr2):
    union_elements = set()
    for num in arr1:
        union_elements.add(num)
    for num in arr2:
        union_elements.add(num)
    # union_elements = list(union_elements)
    # union_elements.sort()
    return f"Union of two Elements are {union_elements} "


if __name__ == "__main__":
    arr1 = list(map(int, input("Array 1: ").split()))
    arr2 = list(map(int, input("Array 2: ").split()))
    print(f"The Array 1 Elements are {arr1} ")
    print(f"The Array 2 Elements are {arr2} ")
    print(UnionOfTwoArrays(arr1, arr2))
