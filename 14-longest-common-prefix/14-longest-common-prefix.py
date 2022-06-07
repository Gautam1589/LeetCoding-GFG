class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=[]
        
        len_=len(min(strs))
        if len_==0:
            return ""
        
        for i in range(1,len(strs)):
            if strs[i][0]!=strs[i-1][0]:
                return ""
        
        ans.append(strs[0][0])
        
        for i in range(1,len_):
            for j in range(1,len(strs)):
                if strs[j][i]!=strs[j-1][i]:
                    return ''.join(ans)
            ans.append(strs[0][i])
        return ''.join(ans)