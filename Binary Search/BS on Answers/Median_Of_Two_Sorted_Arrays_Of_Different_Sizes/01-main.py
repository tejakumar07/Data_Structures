# Brute Force Approach

def medianOfTwoSortedArrays(nums1, nums2):
    n1, n2 = len(nums1), len(nums2)
    n = n1 + n2
    i = j = 0
    arr = []

    while i < n1 and j < n2:
        if nums1[i] <= nums2[j]:
            arr.append(nums1[i])
            i += 1
        else:
            arr.append(nums2[j])
            j += 1

    while i < n1:
        arr.append(nums1[i])
        i += 1

    while j < n2:
        arr.append(nums2[j])
        j += 1

    if n % 2 == 1:
        return float(arr[n // 2])

    return (arr[n // 2] + arr[(n // 2) - 1]) / 2.0
if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(medianOfTwoSortedArrays(nums1, nums2))