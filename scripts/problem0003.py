#!/anaconda3/envs/py37/bin/python

# https://leetcode.com/problems/longest-substring-without-repeating-characters/
from scripts.testhelper import test_assert


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        maxLen = start = 0
        for i, c in enumerate(s):
            if c in map and start <= map[c]:
                start = map[c] + 1
            else:
                maxLen = max(maxLen, i - start + 1)

            map[c] = i

        return maxLen


s = Solution()
test_assert(s.lengthOfLongestSubstring("testting"), 4)
test_assert(s.lengthOfLongestSubstring("abcabcbb"), 3)
test_assert(s.lengthOfLongestSubstring("bbbbb"), 1)
test_assert(s.lengthOfLongestSubstring("pwwkew"), 3)
