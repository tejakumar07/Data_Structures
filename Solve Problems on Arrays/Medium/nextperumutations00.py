#  Brute Force Approach

def NextPermutation(arr):
    import itertools
    perms = sorted(itertools.permutations(arr))
    index = perms.index(tuple(arr))
    next_perm = perms[index+1] if index +1 < len(perms) else perms[0]
    return list(next_perm)

if __name__ == "__main__":
    arr = [3,1,2]
    print(NextPermutation(arr))