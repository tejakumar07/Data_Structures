class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def display(self, head):
        if head is None or head.next is None:
            return head

        itr = head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "--->" if itr.next else str(itr.data)
            itr = itr.next

        return llstr

    def sorting(self, head):
        if head is None or head.next is None:
            return head

        zero_head = Node(-1)
        one_head = Node(-1)
        two_head = Node(-1)

        zero = zero_head
        one = one_head
        two = two_head

        itr = head

        while itr:
            if itr.data == 0:
                zero.next = itr
                zero = zero.next

            elif itr.data == 1:
                one.next = itr
                one = one.next

            else:
                two.next = itr
                two = two.next

            itr = itr.next

        zero.next = one_head.next
        one.next = two_head.next
        two.next = None

        head = zero_head.next

        return head


if __name__ == "__main__":
    ll = LinkedList()
    head = Node(2)
    head.next = Node(0)
    head.next.next = Node(0)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(1)
    print("Orginal Linked List")
    print(ll.display(head))
    print("After Sorting Linked List")
    head = ll.sorting(head)
    print(ll.display(head))
