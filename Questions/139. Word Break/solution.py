class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[0] = True

        wordset =set(wordDict)

        for i in range(len(s) + 1):
            for j in range(i,-1,-1):

                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break

        return dp[len(s)]            