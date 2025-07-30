# Using Binary Search

from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return findMedianSortedArrays(nums2, nums1)
        
        n = n1 + n2
        left = (n1 + n2 + 1) // 2
        low = 0
        high = n1

        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            l1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            r1 = float('inf') if mid1 == n1 else nums1[mid1]
            l2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            r2 = float('inf') if mid2 == n2 else nums2[mid2]

            if l1 > r2:
                high = mid1 -1
            elif l2 > r1:
                low = mid1 + 1
            else:
                if n % 2 == 1:
                    return max(l1, l2)
                return (max(l1, l2) + min(r1, r2)) / 2.0

if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(findMedianSortedArrays(nums1, nums2))