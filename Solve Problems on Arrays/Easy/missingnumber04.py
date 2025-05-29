# Optimal Solution - II
# Best Solution

def MissingNumber(arr, k):
    xor1 = 0
    xor2 = 0
    for i in range(1, k+1):
        xor1 ^= i
    for i in arr:
        xor2 ^= i
    return xor1 ^ xor2

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    d = 7
    print(MissingNumber(arr, d))
