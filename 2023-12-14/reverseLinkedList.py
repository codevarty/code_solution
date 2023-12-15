""" reverseLinkedList.py Leetcode problem: [206] https://leetcode.com/problems/reverse-linked-list """
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        return ListNode(head.val, self.reverseList(head.next))


if __name__ == '__main__':
    sol = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    output = sol.reverseList(head)
    while output is not None:
        print(output.val, end=' ')
        output = output.next
