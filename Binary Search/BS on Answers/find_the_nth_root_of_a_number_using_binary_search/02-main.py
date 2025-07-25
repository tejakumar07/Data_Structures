# Optimal Approach
# Using Binary Search

def find_the_nth_root_of_m(n, m):
    low = 1
    high = m
    
    while low <= high:
        mid = (low + high) // 2
        if mid ** n == m:
            return mid
        elif mid ** n > m:
            high = mid - 1
        else:
            low = mid + 1
    return -1

if __name__ == "__main__":
    
    print(find_the_nth_root_of_m(3, 27))
    print(find_the_nth_root_of_m(4, 69))
    print(find_the_nth_root_of_m(2, 49))
    print(find_the_nth_root_of_m(4, 454))