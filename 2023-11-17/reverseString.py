""" reverseString.py Leetcode problem: [344] https://leetcode.com/problems/reverse-string """
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s = s[::-1]
        print(s)


if __name__ == '__main__':
    sol = Solution()
    sol.reverseString(["h", "e", "l", "l", "o"])
