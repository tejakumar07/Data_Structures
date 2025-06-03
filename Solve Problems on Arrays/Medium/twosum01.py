def TwoSum(arr, target):
    hash_map = {}
    for i in range(len(arr)):
        rem = target - arr[i]
        
        if rem in hash_map:
            return hash_map[rem], i
        hash_map[arr[i]] = i
    return -1, -1



if __name__ == "__main__":
    arr = [1,4,9,14,8,10,3,7]
    target = 22
    print(TwoSum(arr, target))