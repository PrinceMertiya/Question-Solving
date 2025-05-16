class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s= [chars.lower() for chars in s if(chars.isalnum())]

        return s == s[::-1]   