# Better Approach

def MajorityElement(nums):

    hash_map = {}
    n = len(nums) // 2

    for num in nums:
        hash_map[num] = hash_map.get(num, 0) + 1

    for key, value in hash_map.items():
        if value > n:
            return key
    return -1


if __name__ == "__main__":
    arr = [2, 2, 3, 3, 1, 2, 2]
    print(MajorityElement(arr))



# from collections import Counter


# def MajorityElement(nums):
#     hash_map = Counter(nums)
#     for key, value in hash_map.items():
#         if value > len(nums) // 2:
#             return key
#     return -1


# if __name__ == "__main__":
#     arr = [2, 2, 3, 3, 1, 2, 2]
#     print(MajorityElement(arr))