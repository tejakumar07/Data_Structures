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
        
        llstr = ""
        itr = self.head
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
    
    def deleteMiddle(self):
        count = self.traverse()
        
        if count == 1:
            self.head = None
            return
        
        n = count // 2
        
        itr = self.head
        indx = 0
        
        while itr:
            if indx == n - 1:
                itr.next = itr.next.next 
                return
            indx += 1
            itr = itr.next 
        return "Linked List Out of Bound"

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(4)
    ll.head.next.next.next.next = Node(5)
    print(ll.display())
    print(ll.traverse())
    ll.deleteMiddle()
    print(ll.display())