class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        allsol=[]
        currsol=[]
        tel={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        return self.recursive(digits,0,allsol,[],tel)
    
    def recursive(self,digits,i,allsol,currsol,tel):
        if i==len(digits):
            allsol.append(''.join(currsol[:]))
            return
        
        for j in tel[digits[i]]:
            currsol.append(j)
            self.recursive(digits,i+1,allsol,currsol,tel)
            currsol.pop()
        
        return allsol