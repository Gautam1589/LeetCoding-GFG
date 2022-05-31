class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return self.optimize(s,k)
        return self.bruteforce(s,k)
    
    def optimize(self,s,k):
        ans=deque()
        if len(s)<k:
            return False
        
        for i in range(k):
            ans.append(s[i])
        i=0
        set_=set()
        while i+k<len(s):
            set_.add(tuple(ans))
            ans.popleft()
            ans.append(s[i+k])
            i+=1
        set_.add(tuple(ans))
        
        return True if len(set_)==(1<<k) else False
        
    def bruteforce(self,s,k):
        cnt=1<<k
        freq={}
        for i in range(len(s)-k+1):
            if s[i:i+k] not in freq:
                freq[s[i:i+k]]=1
                cnt-=1
                if cnt==0:
                    return True
        return False