

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
    
    def removeNthFromEnd(self, n):
        
        fast = self.head
        
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            self.head = self.head.next
            return
        
        slow = self.head
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        
        slow.next = slow.next.next
        
if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(4)
    ll.head.next.next.next.next = Node(5)
    print(ll.display())
    ll.removeNthFromEnd(2)
    print(ll.display())