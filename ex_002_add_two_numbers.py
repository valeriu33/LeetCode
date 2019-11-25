class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    aux_node = ListNode(0)
    current_node = aux_node
    carry = 0

    while l1 or l2:
        aux1 = l1.val if l1 else 0
        aux2 = l2.val if l2 else 0
        sum = aux1 + aux2 + carry
        carry = sum // 10
        current_node.next = ListNode(sum % 10)
        current_node = current_node.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry > 0:
        current_node.next = ListNode(1)

    return aux_node.next