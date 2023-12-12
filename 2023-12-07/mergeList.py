""" mergeListt.py Leetcode problem: [21] https://leetcode.com/problems/merge-two-sorted-lists """
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        elif not list1 or not list2:
            return list1 or list2
        else:
            tail = dummy = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else :
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            tail.next = list1 or list2
        return dummy.next



if __name__ == '__main__':
    sol = Solution()
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    output = sol.mergeTwoLists(list1, list2)
    while output is not None:
        print(output.val, end=' ')
        output = output.next
