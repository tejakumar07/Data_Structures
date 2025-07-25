# Brute Force Approach
# Using Linear Search

def nth_root_of_give_m(n, m):
    ans = 1
    
    while ans ** n <= m:
        if ans ** n == m:
            return ans
        ans += 1
    return -1

if __name__ == "__main__":
    print(nth_root_of_give_m(3, 27))
    print(nth_root_of_give_m(2, 64))
    print(nth_root_of_give_m(4, 69))