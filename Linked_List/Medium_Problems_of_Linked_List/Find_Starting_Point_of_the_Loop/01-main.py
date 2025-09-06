# Brute Force Approach

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        
        itr = self.head
        count = 0
        
        while itr and count < 10:
            print(itr.data, end = "--->")
            itr = itr.next
            count += 1
        print("None")
    
    def detect_cycle(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        itr = self.head
        mpp = {}
        
        while itr:
            if itr in mpp:
                return itr.data
            
            mpp[itr] =1
            itr = itr.next
        
        return None

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(3)
    ll.head.next = Node(2)
    ll.head.next.next = Node(0)
    ll.head.next.next.next = Node(-4)
    ll.head.next.next.next.next = ll.head.next
    ll.display()
    print(ll.detect_cycle())