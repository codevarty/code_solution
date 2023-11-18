""" mostWord.py Leetcode problem: [344] https://leetcode.com/problems/most-common-word """
import collections
from typing import List
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """ 1. 대소 문자 구분 X
            2. 쉼표, 마침표 구분 X
            3. banned: 문자 제외
        """
        # \w는 특수 문자를 제외한 문자, 숫자 이다.
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
                 if word not in banned]
        # 카운터 객체는 각 리스트 요소와 그 요소의 개수를 tuple 리스트를 반환한다.
        counts = collections.Counter(words)
        # tuple list로 나온다. [(value, count)]
        return counts.most_common(1)[0][0]


if __name__ == '__main__':
    sol = Solution()
    paragraph = "a."
    banned = []

    output = sol.mostCommonWord(paragraph, banned)
    # 정답 확인
    print(output)
