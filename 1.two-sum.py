#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (45.65%)
# Likes:    16367
# Dislikes: 590
# Total Accepted:    3.2M
# Total Submissions: 7M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapIdxNum = {num:idx for idx,num in enumerate(nums)}
        for idx, num in enumerate(nums):
            if target - num in mapIdxNum and idx != mapIdxNum[target - num]:
                return [idx, mapIdxNum[target - num]]
# @lc code=end

