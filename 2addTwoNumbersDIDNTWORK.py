from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLinkedList(node: ListNode):
    while (node != None):
        print(node.val)
        node = node.next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    count=0
    sumLinkedBase10 = ListNode()
    firstNode = sumLinkedBase10

    while (l1 != None)&(l2 != None):
        val10 = (l1.val+l2.val)*(10**count)

        sumLinkedBase10.val = val10

        count += 1
        sumLinkedBase10.next = ListNode()
        sumLinkedBase10 = sumLinkedBase10.next
        l1 = l1.next
        l2 = l2.next


    return firstNode


L1 = ListNode(2, ListNode(4, ListNode(3)))
L11 = ListNode(5, ListNode(6, ListNode(4)))
L111 = addTwoNumbers(L1, L11)
printLinkedList(L111)