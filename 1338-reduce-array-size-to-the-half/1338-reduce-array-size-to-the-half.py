class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        
        n=len(arr)//2
        cnt=0
        limit=len(arr)
        l=[]
        for i in d:
            l.append([i,d[i]])
        l.sort(key=lambda x:x[1], reverse=True)
        
        i=0
        while limit>n:
            limit-=l[i][1]
            cnt+=1
            i+=1
        return cnt
            