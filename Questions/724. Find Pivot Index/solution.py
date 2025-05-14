class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftsum = 0

        for i, num in enumerate(nums):
            if leftsum == total - leftsum - nums[i]:
                return i
            
            leftsum += num

        return -1    

