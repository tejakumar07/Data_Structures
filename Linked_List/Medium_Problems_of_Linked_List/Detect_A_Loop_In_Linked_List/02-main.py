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
        count = 0
        
        while itr and count < 20:
            print(itr.data, end="--->")
            itr = itr.next
            count += 1
        print("None")
    
    def detect_loop(self):
        if self.head is None:
            return "Linked List is Empty"

        slow = self.head
        fast = self.head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast= fast.next.next

            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(4)
    ll.head.next.next.next.next = Node(5)
    ll.head.next.next.next.next.next = Node(6)
    ll.head.next.next.next.next.next.next = Node(7)
    ll.head.next.next.next.next.next.next.next = Node(8)
    ll.head.next.next.next.next.next.next.next.next = Node(9)
    ll.head.next.next.next.next.next.next.next.next.next = ll.head.next.next
    ll.display()
    ans = ll.detect_loop()
    print(ans)