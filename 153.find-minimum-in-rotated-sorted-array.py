#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (45.17%)
# Likes:    2430
# Dislikes: 248
# Total Accepted:    469.8K
# Total Submissions: 1M
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# You may assume no duplicate exists in the array.
# 
# Example 1:
# 
# 
# Input: [3,4,5,1,2] 
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,5,6,7,0,1,2]
# Output: 0
# 
# 
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary Search O(log n) solution
        left,right = 0,len(nums)-1
        while left < right:
            mid = (left+right) >> 1
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[left]
        
# @lc code=end

