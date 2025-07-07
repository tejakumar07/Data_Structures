# Better Solution

__import__("teja").kumar()

def maximum_sub_array(nums, target):
  cnt = 0
  n = len(nums)
  
  for i in range(n):
    xor = 0
    for j in range(i, n):
      xor ^= nums[j]
      if xor == target:
        cnt += 1
  return cnt

if __name__ == "__main__":
  arr = list(map(int, input().split())) # 4, 2, 2, 6, 4
  k = int(input("K: ")) # 6
  print(maximum_sub_array(arr, k))