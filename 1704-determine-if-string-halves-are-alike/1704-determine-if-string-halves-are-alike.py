class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        d=set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        i,j=0,len(s)-1
        c1,c2=0,0
        while i<j:
            if s[i] in d:
                c1+=1
            if s[j] in d:
                c2+=1
            i+=1
            j-=1
        
        return True if c1==c2 else False
        