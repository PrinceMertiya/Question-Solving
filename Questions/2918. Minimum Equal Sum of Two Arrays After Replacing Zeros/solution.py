class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 , s2 = sum(nums1),sum(nums2)
        num_zero_s1 , num_zero_s2 = nums1.count(0), nums2.count(0)


        if num_zero_s1 == 0 or num_zero_s2 == 0:
            if num_zero_s1 == num_zero_s2:

                return -1 if s1 != s2 else s1  
            
            elif num_zero_s1 == 0:
                return s1 if s1  >= s2 + num_zero_s2 else -1

            elif num_zero_s2 == 0:
                return s2 if num_zero_s1 + s1 <= s2 else -1


        return max(s1 + num_zero_s1,s2 + num_zero_s2)       