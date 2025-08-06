def longestCommonPrefix(strs):
    import os
    ans = os.path.commonprefix(strs)
    return ans

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    print(longestCommonPrefix(strs))