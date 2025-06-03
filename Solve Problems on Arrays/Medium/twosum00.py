def TwoSum(arr, target):
    for i, num1 in enumerate(arr):
        for j, num2 in enumerate(arr):
            if num1 + num2 == target:
                return i, j
    return -1, -1

if __name__ == "__main__":
    arr = [1,4,9,14,8,10,3,7]
    target = 22
    print(TwoSum(arr, target))