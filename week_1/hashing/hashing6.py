def character_frequency(name):
    hash = [0]*26
    for i in range(len(name)):
        if 'a' <= name[i] <= 'z':
            hash[ord(name[i]) -ord('a')] += 1
    return hash

def query_frequency(hash,query):
    for q in query:
        if 'a' <= q <= 'z':
            print(hash[ord(q) - ord('a')])

def main():
    name = input("Name: ").lower().strip()
    query = input("Query: ").lower().strip()
    hash = character_frequency(name)
    query_frequency(hash,query)

if __name__ == "__main__":
    main()