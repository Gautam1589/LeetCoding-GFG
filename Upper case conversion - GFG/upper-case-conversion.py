#User function Template for python3

class Solution:
    def transform(self, s):
        # code here
        l=list(s)
        l[0]=l[0].upper()
        i=1
        while i<len(s):
            if l[i]==' ':
                l[i+1]=l[i+1].upper()
                i+=2
            else:
                i+=1
        return ''.join(l)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        print(ob.transform(s))
# } Driver Code Ends