# Brute Force Approach

__import__("teja").kumar()

def maximum_sub_array(nums, target):
  cnt = 0
  n = len(nums)
  for i in range(n):
    for j in range(i, n):
      xor = 0
      for k in range(i, j+1):
        xor ^= nums[k]
      if xor == target:
        cnt += 1
  return cnt
if __name__ == "__main__":
  arr = [4, 2, 2, 6, 4]
  print(maximum_sub_array(arr, 6))