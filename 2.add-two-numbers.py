#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (33.96%)
# Likes:    8899
# Dislikes: 2245
# Total Accepted:    1.5M
# Total Submissions: 4.4M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1sum, l2sum = '', ''
        
        while l1 != None:
            l1sum += str(l1.val)
            l1 = l1.next

        while l2 != None:
            l2sum += str(l2.val)
            l2 = l2.next
        
        l1sum, l2sum = l1sum[::-1], l2sum[::-1]
        twoSum = str(int(l1sum) + int(l2sum))[::-1]
        
        head = ListNode(twoSum[0])
        tail = head
        for idx in range(1,len(twoSum)):
            tail.next = ListNode(twoSum[idx])
            tail = tail.next
        return head

# @lc code=end

