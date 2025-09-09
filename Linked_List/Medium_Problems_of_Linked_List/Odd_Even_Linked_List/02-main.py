# Optimal Approach

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

    def oddEvenList(self):
        if self.head is None or self.head.next is None:
            return self.head
        
        odd = self.head
        even = even_head = self.head.next
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
        
        odd.next = even_head
            
    
if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(2)
    ll.head.next = Node(1)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(5)
    ll.head.next.next.next.next = Node(6)
    ll.head.next.next.next.next.next = Node(4)
    ll.head.next.next.next.next.next.next = Node(7)
    print(ll.display())
    ll.oddEvenList()
    print(ll.display())