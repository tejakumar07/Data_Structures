# optimal solution


def solve(str):
    n = len(str)
    
    if n == 0:
        return 0
    
    hash_map = [-1] * 256
    l = r = 0
    maxi = -1
    
    while r < n:
        if hash_map[ord(str[r])] != -1:
            if hash_map[ord(str[r])] >= l:
                l = hash_map[ord(str[r])] +1
        hash_map[ord(str[r])] = r
        length = r - l + 1
        maxi = max(maxi, length)
        r += 1
    return maxi            
if __name__ == "__main__":
    str = "cadbzabcd"
    print("The length of the longest substring without repeating characters is", solve(str))