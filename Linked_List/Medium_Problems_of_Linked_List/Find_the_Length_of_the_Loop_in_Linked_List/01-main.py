class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        itr = self.head
        
        count = 0
        while itr and count < 10:
            print(itr.data, end = "--->")
            itr = itr.next
            count += 1
        print("None")
    
    def detect_length_loop(self):
        
        itr = self.head
        mpp = {}
        timer = 1
        
        while itr:
            if itr in mpp:
                length = timer - mpp[itr]
                return length
            
            mpp[itr] = timer
            timer += 1
            itr = itr.next
        
        return None
            
if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(4)
    ll.head.next.next.next.next = Node(5)
    ll.head.next.next.next.next.next = ll.head.next
    ll.display()
    ll.detect_length_loop()
    ans = ll.detect_length_loop()
    print(ans)