def longestCommonPrefix(strs):
    n = len(strs)
    if n == 1:
        return strs[0]
    strs.sort()
    first = strs[0]
    last = strs[-1]
    indx = 0
    n = len(first)
    
    while indx < n:
        if first[indx] != last[indx]:
            return first[0:indx]
        indx += 1
    return first[0:indx]

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(longestCommonPrefix(strs))