class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        res = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):

                    if i == j  or j==k or k==i:
                        continue

                    if digits[i] == 0:
                        continue

                    if(digits[k] % 2 != 0):
                        continue

                    
                    s = digits[i] * 100 + digits[j] * 10+ digits[k]
                    res.add(s)

                    

        return sorted(res)                