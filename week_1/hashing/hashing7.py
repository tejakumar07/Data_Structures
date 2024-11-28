def character_frequency(name):
    hash = [0] * 256  # Array to store frequencies for all ASCII characters
    
    for i in range(len(name)):
        hash[ord(name[i])] += 1  # Use the character to get its ASCII value
    return hash

def query_frequency(hash, query):
    for q in query:
        value = ord(q)  # Get the ASCII value of the character
        print(f"'{q}' (ASCII {value}) appears {hash[value]} times.")

def main():
    text = input("Text: ")
    query = input("Query: ")
    if not text.strip() or not query.strip():
        print("Please try again...")
        return
    frequency = character_frequency(text)
    query_frequency(frequency, query)

if __name__ == "__main__":
    main()