# Brute Force Approach

def LargestElement(arr):
    arr.sort()
    return arr[-1]

if __name__ == "__main__":
    arr = list(map(int, input("Array: ").split()))
    print(LargestElement(arr))
