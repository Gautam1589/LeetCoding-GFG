class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=self.solve(s,[])
        t1=self.solve(t,[])
        
        return s1==t1
    
    def solve(self,s,stack):
        for i in s:
            if i!='#':
                stack.append(i)
            elif stack:
                stack.pop()
                
        return ''.join(stack)