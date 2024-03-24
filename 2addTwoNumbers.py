from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printLinkedList(node: ListNode):
    while (node != None):
        print(node.val)
        node = node.next


def getSumBase10LinkedLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> int:
    count = 0
    sumBase10 = 0
    
    # Acá tengo que checkear si se da la situacion que uno esté vacio pero el otro no
    while (l1 != None) or (l2 != None):
        if l1 == None:
            sumBase10 += (l2.val)*(10**count)
            l2 = l2.next

        elif l2 == None:
            sumBase10 += (l1.val)*(10**count)
            l1 = l1.next

        else:
            sumBase10 += (l1.val+l2.val)*(10**count)
            l1 = l1.next
            l2 = l2.next

        count += 1

    return sumBase10


def base10ToLinkedList(num: int) -> Optional[ListNode]:

    base10Linked = ListNode()
    firstNode = base10Linked
    base = 10
    count = 0

    while (num%(base/10))!=num:
        base10Linked.val = int(((num%base)-base10Linked.val)//(base/10))
        base10Linked.next = ListNode()
        base10Linked = base10Linked.next

        base = base*10
        count += 1

    return firstNode


# INEFFICIENT:
# one traversal to get the sum in base 10 off the two linked lists, and another traversal to put that number in a linked list
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    return base10ToLinkedList( getSumBase10LinkedLists(l1, l2) )


L1 = ListNode(2, ListNode(4, ListNode(3)))
L11 = ListNode(5, ListNode(6, ListNode(4)))

L2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
L22 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
printLinkedList(addTwoNumbers(L2, L22))
print("------------")
printLinkedList(addTwoNumbers(L1, L11))
