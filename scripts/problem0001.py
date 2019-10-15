#!/anaconda3/envs/py37/bin/python

# https://leetcode.com/problems/two-sum/
from typing import List

from scripts.time_measure import time_it


class Solution:
    @time_it
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            #print(str(i) + " " + str(nums[i]))
            if nums[i] in map:
                return [map.get(nums[i]), i]
            map[target - nums[i]] = i;
        return [-1, -1]


s = Solution()
print(s.twoSum([1,2,4,8], 5))
print(s.twoSum([2, 7, 11, 15], 9))
