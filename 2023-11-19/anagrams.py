""" anagrams.py Leetcode problem: [49] https://leetcode.com/problems/group-anagrams """
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 리스트를 기본값으로 가지는 defaultdict 생성
        d = collections.defaultdict(list)
        for word in strs:
            # defaultdict에 키가 없으면 defualt value를 생성한다.
            d[''.join(sorted(word))].append(word)
        return list(d.values())


if __name__ == '__main__':
    sol = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    output = sol.groupAnagrams(strs)
    print(output)