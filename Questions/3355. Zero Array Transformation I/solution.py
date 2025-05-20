class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        m = [0] * (len(nums) + 1)
        for l,r in queries:
            m[l] += 1
            m[r + 1] -= 1
        s = 0
        for x ,y in zip(nums,m):
            s += y
            if x > s:
                return False
        return True
         