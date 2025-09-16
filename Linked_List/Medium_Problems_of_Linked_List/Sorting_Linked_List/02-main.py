class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None


class LinkedList:
    def display(self, head):
        if head is None:
            return "Linked List is Empty"

        itr = head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "--->" if itr.next else str(itr.data)
            itr = itr.next

        return llstr

    def find_middle(self, head):
        if head is None or head.next is None:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge_sorted_linked_list(self, list1, list2):
        dummy_node = Node(-1)
        temp = dummy_node

        while list1 is not None and list2 is not None:
            if list1.data <= list2.data:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        while list1 is not None:
            temp.next = list1
            list1 = list1.next
            temp = temp.next

        while list2 is not None:
            temp.next = list2
            list2 = list2.next
            temp = temp.next

        return dummy_node.next

    def merge_linked_list(self, head):
        if head is None or head.next is None:
            return head

        middle = self.find_middle(head)
        left = head
        right = middle.next
        middle.next = None

        left = self.merge_linked_list(left)
        right = self.merge_linked_list(right)

        return self.merge_sorted_linked_list(left, right)


if __name__ == "__main__":
    ll = LinkedList()
    head = Node(14)
    head.next = Node(2)
    head.next.next = Node(56)
    head.next.next.next = Node(12)
    head.next.next.next.next = Node(1)
    head.next.next.next.next.next = Node(32)
    print("Orginal Linked List")
    print(ll.display(head))
    print("After Sorting Linked List")
    head = ll.merge_linked_list(head)
    print(ll.display(head))
