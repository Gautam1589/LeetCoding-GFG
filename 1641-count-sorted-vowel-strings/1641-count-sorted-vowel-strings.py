class Solution:
    def countVowelStrings(self, n: int) -> int:
        self.allsol=0
        vowels=["a","e","i","o","u"]
        return self.dp_table(n,vowels)
        #self.recursive(n,0,vowels)
        #self.backtrack(n,vowels,[])
        #return self.allsol
    
    def dp_table(self,n,vowels):
        dp=[1]*5
        
        while n-1:
            for i in range(3,-1,-1):
                dp[i]+=dp[i+1]
            
            n-=1
        return sum(dp)
        
    
    #TLE
    def recursive(self,n,last,vowels):
        if n==0:
            self.allsol+=1
            return
        
        for i in range(len(vowels)):
            if i>=last:
                self.recursive(n-1,i,vowels)
                
    #TLE
    def backtrack(self,n,vowels,currsol):
        if len(currsol)==n:
            self.allsol+=1
            return
        
        for i in vowels:
            if len(currsol)==0 or currsol[-1]<=i:
                currsol.append(i)
                self.backtrack(n,vowels,currsol)
                currsol.pop()
            