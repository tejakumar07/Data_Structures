# Brute Force Approach

def kthElement(arr1: list, n: int, arr2: list, m: int, k: int) -> int:
    i = j = 0
    merged = []

    
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    
    while i < n:
        merged.append(arr1[i])
        i += 1

    while j < m:
        merged.append(arr2[j])
        j += 1

    
    return merged[k - 1]


if __name__ == "__main__":
    arr1 = [2, 3, 45]
    arr2 = [4, 6, 7, 8]
    k = 4
    n = len(arr1)
    m = len(arr2)
    ans = kthElement(arr1, n, arr2, m, k)
    print(ans)