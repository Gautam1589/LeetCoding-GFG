class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        row,col,diag,anti={},{},{},{}
        
        lamp=set()
        for i in lamps:
            lamp.add((i[0],i[1]))
            
        for i in lamp:
            row[i[0]]=row.get(i[0],0)+1
            col[i[1]]=col.get(i[1],0)+1
            d=i[0]-i[1]
            a=i[0]+i[1]
            diag[d]=diag.get(d,0)+1
            anti[a]=anti.get(a,0)+1
        
        #print(row,col,diag,anti,lamp)
        dirn=[(0,0),(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1)]
        
        ans=[]
        for j in queries:
            r,c=j[0],j[1]
            d,a=r-c,r+c
            if (r in row and row[r]>0) or (c in col and col[c]>0) or (d in diag and diag[d]>0) or (a in anti and anti[a]>0):
                ans.append(1)
            else:
                ans.append(0)
            
            for i in dirn:
                I=r+i[0]
                J=c+i[1]
                if I<0 or J<0 or I>=n or J>=n:
                    continue
                if (I,J) in lamp:
                    row[I]-=1
                    col[J]-=1
                    diag[I-J]-=1
                    anti[I+J]-=1
                    lamp.remove((I,J))
            #print(row,col)
        
        return ans