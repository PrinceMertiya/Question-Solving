
def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashed_map = {}

        for i, val in enumerate(nums):

            complement = target - val

            if complement in hashed_map:

                return (hashed_map[complement] , i )

            hashed_map[val] = i

        return []       