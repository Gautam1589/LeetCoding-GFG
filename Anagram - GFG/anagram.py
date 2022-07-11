#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        d1={}
        for i in a:
            d1[i]=d1.get(i,0)+1
        for i in b:
            if i in d1:
                d1[i]+=1
            else:
                return False
        
        if len(a)!=len(b):
            return False
            
        for i in d1:
            if d1[i]&1:
                return False
        return True
        
        #O(N) time and O(2*N) space
        # d1={}
        # for i in a:
        #     d1[i]=d1.get(i,0)+1
        # d2={}
        # for i in b:
        #     d2[i]=d2.get(i,0)+1
            
        # if len(d1)!=len(d2):
        #     return False
        
        # for i in d1:
        #     if i not in d2 or d1[i]!=d2[i]:
        #         return False
        # return True

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends