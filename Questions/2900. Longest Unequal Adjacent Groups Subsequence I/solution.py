class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        last = -1
        result= []
        for i in range(len(words)):
            if(groups[i] != last):
                result.append(words[i])
                last = groups[i]

        return result

