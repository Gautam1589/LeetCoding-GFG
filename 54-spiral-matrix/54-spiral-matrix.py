class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        I,J=0,0
        m=len(matrix)
        n=len(matrix[0])
        res=[]
                
        while I<m-1 and J<n-1:
            i,j=I,J
    
            while j<n-1:
                res.append(matrix[I][j])
                j+=1
        
            while i<m-1:
                res.append(matrix[i][n-1])
                i+=1
            
            while j>J:
                res.append(matrix[m-1][j])
                j-=1
        
            while i>I:
                res.append(matrix[i][J])
                i-=1
            
            I+=1
            J+=1
            m-=1
            n-=1

        if I==m-1 and J==n-1:
            res.append(matrix[I][J])
        elif J==n-1:
            for i in range(I,m):
                res.append(matrix[i][J])
        elif I==m-1:
            for j in range(J,n):
                res.append(matrix[I][j])
        
        return res
