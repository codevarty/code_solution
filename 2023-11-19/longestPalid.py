""" longestPalid.py Leetcode problem: [5] https://leetcode.com/problems/longest-palindromic-substring """
import math


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1 or s[:] == s[::-1]:
            return s

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        result = ''
        for i in range(len(s)-1):
            result = max(result, expand(i, i+1), expand(i, i+2), key=len)
        return result


if __name__ == '__main__':
    sol = Solution()
    s = "babad"
    output = sol.longestPalindrome(s)
    print(output)
