# [Hashing] -> Prestoring / Fetching

n = 5
array = list(map(int, input("Numbers: ").split()))

q = 5
query = list(map(int, input("Query: ").split()))


hash = [0] * 13  
for i in range(n):
    hash[array[i]] += 1
for q in query:
    if 0 <= q < len(hash):
        print(hash[q])
    else:
        print(0)
