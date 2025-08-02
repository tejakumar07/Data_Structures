def isPalindrome(str):
    n = len(str)
    i, j = 0, n - 1
    
    while i < j:
        
        while i < j and not str[i].isalnum():
            i += 1
        while i < j and not str[j].isalnum():
            j -= 1
        
        if str[i].lower() != str[j].lower():
            return False
        
        i += 1
        j -= 1
    
    return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))