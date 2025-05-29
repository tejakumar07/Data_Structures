def MoveZerosToEnd(arr):
    non_zero = []
    for num in arr:
        if num != 0:
            non_zero.append(num)
    zero_length = len(arr) - len(non_zero)
    result = non_zero + [0] * zero_length
    return result

if __name__ == "__main__":
    arr = [1,0,2,0,3,0,5,0,4,0]
    print(MoveZerosToEnd(arr))
