class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        if self.head is None:
            return 0
        
        itr = self.head
        count = 0
        
        while itr:
            count += 1
            itr = itr.next 
        
        return count
    
    def display(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        
        itr = self.head
        
        while itr:
            print(itr.data, end = "->")
            itr = itr.next
    

    def middle_element(self):
        n = self.traverse()
        if n % 2 == 1:
            n = n // 2
        else:
            n = (n // 2) + 1
        itr = self.head
        count = 0
        
        while itr:
            if n == count:
                return itr.data
            itr = itr.next 
            count += 1
        return None

if __name__ == "__main__":
    ll = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5= Node(5)
    ll.head = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    ans = ll.traverse()
    print(ans)
    ans_1 = ll.middle_element()
    print(ans_1)
    ll.display()