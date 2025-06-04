class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        one = 1
        two = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != '0':
                current = one    
            value = int(s[i-1:i+1])
            if 10 <= value <= 26:
                current += two
            two = one
            one = current
        return one
