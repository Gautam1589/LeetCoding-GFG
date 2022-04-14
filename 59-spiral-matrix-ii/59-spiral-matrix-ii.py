class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        I,J=0,0
        res=[[0]*n for i in range(n)]
        val=1

        while I<n-1 or J<n-1:
            i,j=I,J
    
            while j<n-1:
                res[I][j]=val
                val+=1
                j+=1
        
            while i<n-1:
                res[i][n-1]=val
                val+=1
                i+=1
            
            while j>J:
                res[n-1][j]=val
                val+=1
                j-=1
        
            while i>I:
                res[i][J]=val
                val+=1
                i-=1
            
            I+=1
            J+=1
            n-=1
        
        if I==J and I!=n:
            res[I][J]=val
        
        return res