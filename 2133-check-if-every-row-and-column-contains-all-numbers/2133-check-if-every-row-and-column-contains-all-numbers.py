class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        r={i:set() for i in range(n)}
        c={i:set() for i in range(n)}
    
        for i in range(n):
            for j in range(n):
                if len(r[i])!=0:
                    for k in r[i]:
                        if matrix[i][j]==k:
                            return False
                elif len(c[j])!=0:
                    for k in c[j]:
                        if matrix[i][j]==k:
                            return False
                r[i].add(matrix[i][j])
                c[j].add(matrix[i][j])
        
        for i in r:
            if len(r[i])!=n:
                return False
        for j in c:
            if len(c[j])!=n:
                return False
        #print(r,c)        
        return True
                