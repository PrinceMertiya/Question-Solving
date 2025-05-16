# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = head
        fast = head
        count = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None    
           
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left = head
        right = prev
        max_sum = 0 

        while right:
            total = left.val + right.val
            max_sum = max(total,max_sum)
            left = left.next
            right = right.next

        return max_sum        
        