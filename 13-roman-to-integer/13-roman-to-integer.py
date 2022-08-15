class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        out=0
        while i<len(s):
            while i+1<len(s) and s[i]==s[i+1]:
                out+=d[s[i]]
                i+=1
            if i+1<len(s) and d[s[i]]<d[s[i+1]]:
                out+=d[s[i+1]]-d[s[i]]
                i+=2
            else:
                out+=d[s[i]]
                i+=1
        return out
        