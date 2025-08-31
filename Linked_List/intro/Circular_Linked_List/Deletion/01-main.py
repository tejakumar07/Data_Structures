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

    def delete_at_index(self, index):
        if self.head is None:
            print("List is Empty")
            return

        # Case 1: Delete head node
        if index == 0:
            # Only one node
            if self.head.next == self.head:
                self.head = None
                return

            # Find last node
            last = self.head
            while last.next != self.head:
                last = last.next

            # Make last node point to next of head
            last.next = self.head.next
            self.head = self.head.next
            return

        # Case 2: Delete non-head node
        temp = self.head
        count = 0
        prev = None
        while count < index:
            prev = temp
            temp = temp.next
            count += 1
            # If we looped back → index out of range
            if temp == self.head:
                print("Index out of range")
                return

        prev.next = temp.next

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

cll.display()          # 10 -> 20 -> 30 -> 40
cll.delete_at_index(0) # delete head
cll.display()          # 20 -> 30 -> 40
cll.delete_at_index(1) # delete index 1 (30)
cll.display()          # 20 -> 40
cll.delete_at_index(5) # invalid
