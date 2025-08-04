def strStr(haystack, needle):
    
    ans = -1
    if len(needle) > len(haystack):
        return ans
    
    if needle in haystack:
        ans = haystack.find(needle)
    
    return ans
if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "but"
    print(strStr(haystack, needle))