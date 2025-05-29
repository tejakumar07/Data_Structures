def prestoring():
    length = len(array)
    hash = [0] * 25
    for i in range(length):
        hash[array[i]] += 1
    return hash
def fetching(hash):
    for q in query:
        if 0 < q <= hash[q]:
            print(q)
        else:
            print(0)


if __name__ == "__main__":
    array = [1,2,3,1,5,6,3,9,4,10,6,2,7]
    query = [1,2,4,7,10]
    hash = prestoring()
    fetching(hash)