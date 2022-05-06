class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        for i in s:
            if not stack:
                stack.append([i,1])
            elif stack[-1][0]!=i:
                stack.append([i,1])
            else:
                stack[-1][1]+=1
            
            if stack[-1][1]==k:
                stack.pop()
        
        ans=[]
        while stack:
            ans.extend(stack[-1][0]*stack[-1][1])
            stack.pop()
            
        ans=ans[::-1]
        return ''.join(ans)