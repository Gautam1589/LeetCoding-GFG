class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        s=palindrome
        n = len(s)
        flag=0
        if n == 1:
            return ''
        for i in range(n//2):
            if s[i] != 'a':
                return s[:i] + 'a' + s[i+1:]
                flag=1
        return s[:-1] + 'b'