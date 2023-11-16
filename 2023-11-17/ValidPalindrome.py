""" ValidPalindrome.py Leetcode problem: [125] https://leetcode.com/problems/valid-palindrome """
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # string delete not alpha or num
        sb = re.sub('[^a-zA-Z0-9]', '', s)
        s = sb.lower()
        # s ==  (reverse)s
        return s == s[::-1]


if __name__ == '__main__':
    sol = Solution()
    test_input = "A man, a plan, a canal: Panama"
    output = sol.isPalindrome(test_input)
    print(output)