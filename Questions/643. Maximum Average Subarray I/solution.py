class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        total = sum(nums[:k])
        pre_sum = total

        for i in range(k,len(nums)):
            total += nums[i] - nums[i - k]
            pre_sum = max(total,pre_sum)

        return  pre_sum / k    
        