#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (46.61%)
# Likes:    8594
# Dislikes: 406
# Total Accepted:    1.1M
# Total Submissions: 2.3M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1: return nums[0]
        dp = [nums[0]]+[0]*(length-1)
        for i in range(1,length):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        return max(dp)

# @lc code=end

