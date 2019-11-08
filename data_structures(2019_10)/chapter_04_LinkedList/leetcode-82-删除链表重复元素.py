# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:
            head = head.next
        if not head:
            return None
        prev = head
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return head

    def removeElements_by_dummy_head(self, head: ListNode, val: int) -> ListNode:
        dummy_head = ListNode(None)
        dummy_head.next = head

        prev = dummy_head
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy_head.next

    def removeElements_by_recursion(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        head.next = self.removeElements_by_recursion(head.next, val)
        # return head.next if head.val == val else head
        res = self.removeElements_by_recursion(head.next, val)
        if head.val == val:
            return res
        else:
            head.next = res
        return head




