# When a function call itself, untill a specific condition is met

def charlie(to,count):
    if count == 5:  # This is Called The Base Condition
        return
    print("Hello, world!",to)
    charlie(to,count+1)
if __name__ == "__main__":
    name = "Teja"
    n =0
    charlie(name,n)