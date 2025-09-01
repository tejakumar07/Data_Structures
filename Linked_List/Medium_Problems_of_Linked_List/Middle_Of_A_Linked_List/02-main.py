# using algorithm called 
# tortoise and hare
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
        llstr = ""
        while itr:
            llstr += str(itr.data) + "--->" if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
    
    def finding_middle_element(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
        
if __name__ == "__main__":
    ll = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    ll.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    ll.display()
    ll.finding_middle_element()