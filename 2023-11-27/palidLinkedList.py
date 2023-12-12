"""paildLinkedList.py Leetcode problem: [234] https://leetcode.com/problems/palindrome-linked-list """
from typing import Optional, Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            # slow와 역순을 비교한다.
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next

        return not rev # None이 되어야 True이다.


if __name__ == '__main__':
    sol = Solution()
    node = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    output = sol.isPalindrome(node)
    print(output)
