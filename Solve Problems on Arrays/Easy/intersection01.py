def Intersection(arr1, arr2):
    i, j = 0, 0
    m, n = len(arr1), len(arr2)
    ans = []
    while (i < m and j < n):
        if arr1[i] < arr2[j]:
            i+=1
        elif arr1[i] > arr2[j]:
            j+= 1
        else:
            ans.append(arr1[i])
            i+=1
            j+=1
    return ans

if __name__ == "__main__":
    arr1 = [1,2,3,3,4]
    arr2 = [1,2,3,3]
    print(Intersection(arr1,arr2))
