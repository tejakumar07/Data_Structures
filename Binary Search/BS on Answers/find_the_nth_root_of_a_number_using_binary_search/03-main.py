def multiply(mid, n, m): # mid = 14, n = 3, m = 27
    result = 1
    for _ in range(n):
        result *= mid
        if result > m:
            return result  # Early exit if result exceeds m
    return result

def find_the_nth_root_of_m(n, m):
    low, high = 1, m

    while low <= high:
        mid = (low + high) // 2
        mid_pow = multiply(mid, n, m)

        if mid_pow == m:
            return mid
        elif mid_pow < m:
            low = mid + 1
        else:
            high = mid - 1

    return -1 

if __name__ == "__main__":
    print(find_the_nth_root_of_m(3, 27))
    print(find_the_nth_root_of_m(4, 69))
    print(find_the_nth_root_of_m(2, 49))
    print(find_the_nth_root_of_m(4, 454))
