""" log.py Leetcode problem: [937] https://leetcode.com/problems/reorder-data-in-log-files/ """
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter, digit = [], []
        # letter-code digit-code distribute
        for log in logs:
            if log.split()[1].isdigit():
                digit.append(log)
            else:
                letter.append(log)
        # Sort identifiers in order
        letter.sort(key=lambda x: x.split()[0])
        # sort lexicographically
        letter = sorted(letter, key=lambda x: x.split()[1:])
        return letter+digit


if __name__ == '__main__':
    sol = Solution()
    input = ["dig1 8 1 5 1","let2 art can","dig2 3 6","let1 art can","let3 art zero"]
    output = sol.reorderLogFiles(input)
    print(output)