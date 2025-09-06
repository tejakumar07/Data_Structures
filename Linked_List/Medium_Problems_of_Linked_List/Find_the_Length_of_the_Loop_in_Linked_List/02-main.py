# Optimal Approach

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        itr = self.head
        count = 0

        while itr and count < 10:
            print(itr.data, end = "--->")
            count += 1
            itr = itr.next
        print("None")

    def find_length(self, slow, fast):
        count = 1
        fast = fast.next
        while fast != slow:
            fast = fast.next
            count += 1

        return count

    def detect_the_length_of_loop(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return self.find_length(slow, fast)

        return 0
if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(1)
    ll.head.next = Node(2)
    ll.head.next.next = Node(3)
    ll.head.next.next.next = Node(4)
    ll.head.next.next.next.next = Node(5)
    ll.head.next.next.next.next.next = Node(6)
    ll.head.next.next.next.next.next.next = ll.head.next
    ll.display()
    ans = ll.detect_the_length_of_loop()
    print(ans)
