# In this let's talk about the Global Variable and Local Variable in the Hashing
"""
Global Hash: Can Be very big, like [0] * (10**7). It works because it uses heap memory

Local Hash: Smaller, like [0] * (10**6) it's limited by stack memory

Global Variables uses more meomory
Local variables are limited

"""

hash_global = [0] * (10**7)
print("length of the Global Hash is: ",len(hash_global))

def created_local_hash():
    try:
        # Local Hash
        hash_local = [0] * (10**6)
        print("Length of Local Hash",len(hash_local))
    except MemoryError:
        print("Local Hash is Very Big")

created_local_hash()

def created_large_local_hash():
    try:

        hash_local = [0] * (10**10) #It support's up to 10^9
        print("The length of local hash is too big :",len(hash_local))
    except MemoryError:
        print("Local Hast is too big ,cause MemoryError")
created_large_local_hash()