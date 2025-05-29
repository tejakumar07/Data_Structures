# Better Approach

def Function(arr):
    maximum = max(arr)
    hash_freq = [0] * (maximum +1)
    for i in range(0, len(arr)):
        hash_freq[arr[i]] += 1
    for i in range(1, len(hash_freq)):
        if hash_freq[i] == 1:
            return i
if __name__ == "__main__":
    arr = [1,1,2,2,3,3,5,5,6,6,7,8,8]
    print(Function(arr))
