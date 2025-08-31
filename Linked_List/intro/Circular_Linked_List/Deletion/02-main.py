class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Circular Linked List is Empty")
            return

        itr = self.head
        result = []
        while True:
            result.append(str(itr.data))
            itr = itr.next
            if itr == self.head:
                break
        print(" -> ".join(result))

    def delete_by_value(self, value):
        if self.head is None:
            print("List is Empty")
            return

        # Case 1: Head node has the value
        if self.head.data == value:
            # Only one node in list
            if self.head.next == self.head:
                self.head = None
                return

            # Find last node
            last = self.head
            while last.next != self.head:
                last = last.next

            # Point last.next to head.next
            last.next = self.head.next
            self.head = self.head.next
            return

        # Case 2: Non-head node
        prev = self.head
        curr = self.head.next

        while curr != self.head:
            if curr.data == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

        print("Value not found")
cll = CircularLinkedList()

# Manually creating list: 10 -> 20 -> 30 -> 40 -> (back to 10)
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

cll.head = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = cll.head

cll.display()              # 10 -> 20 -> 30 -> 40
cll.delete_by_value(10)    # delete head (10)
cll.display()              # 20 -> 30 -> 40
cll.delete_by_value(30)    # delete middle node
cll.display()              # 20 -> 40
cll.delete_by_value(100)   # not found
