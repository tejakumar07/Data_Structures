def strStr(haystack, needle):
    if needle == "":
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i : i + len(needle)] == needle:
            return i

    return -1

if __name__ == "__main__":
    haystack = "sadbutsad"
    needle = "but"
    print(strStr(haystack, needle))