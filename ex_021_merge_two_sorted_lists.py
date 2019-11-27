from typing import List


class ListNode:
    def __init__(self, x):
        if x:
            self.val = x
            self.next = None

    def __str__(self):
        s = ""
        aux = self
        while aux:
            s += str(aux.val)
            aux = aux.next
        return s

    @classmethod
    def from_list(cls, arr: List[int]) -> "ListNode":
        node = ListNode(0)
        initial_node = node
        for i in range(len(arr)):
            node.next = ListNode(arr[i])
            node = node.next
        return initial_node.next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    temp_node = ListNode(0)
    response_node = temp_node
    while l1 and l2:
        if l1.val <= l2.val:
            temp_node.next = ListNode(l1.val)
            l1 = l1.next
        else:
            temp_node.next = ListNode(l2.val)
            l2 = l2.next
        temp_node = temp_node.next
    if l1:
        temp_node.next = l1
    elif l2:
        temp_node.next = l2

    return response_node.next
