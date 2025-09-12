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
            return "Linked List is Empty"
    
        itr = self.head
        llstr = ""
        
        while itr:
            llstr += str(itr.data) + "--->" if itr.next else str(itr.data)
            itr = itr.next
        
        return llstr

    def traverse(self):
        count = 0
        
        if self.head is None:
            return count
        
        itr = self.head
        
        while itr:
            count += 1
            itr = itr.next
        
        return count
    
    def removeNthFromEnd(self, n):
        total =  self.traverse()
        total = total - n
        
        if total == 0:
            self.head = self.head.next
            return
        
        indx = 0
        itr = self.head
        
        while itr:
            if indx == total - 1:
                itr.next = itr.next.next
                return
            indx += 1
            itr = itr.next
        
        return "Linked List out of bound"

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(4)
    ll.head.next.next.next.next = Node(5)
    print(ll.display())
    print(ll.traverse())
    ll.removeNthFromEnd(2)
    print(ll.display())