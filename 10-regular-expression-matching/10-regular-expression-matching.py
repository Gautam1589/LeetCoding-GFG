class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #built-in function
        regex=re.compile(p)
        if regex.fullmatch(s):
            return True
        return False