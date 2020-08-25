#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (26.92%)
# Likes:    7677
# Dislikes: 859
# Total Accepted:    1M
# Total Submissions: 3.7M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: 
            return None
        res = []
        nums = sorted(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            m, r = i + 1, len(nums) - 1
            while m < r:
                s = nums[i] + nums[m] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[m], nums[r]])
                    m += 1
                    r -= 1
                    while m < r and nums[m] == nums[m - 1]: m += 1
                    while m < r and nums[r] == nums[r + 1]: r -= 1
                elif s < 0:
                    m += 1
                else:
                    r -= 1
        return res  


# @lc code=end

