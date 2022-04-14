class Solution:
    def countPrimes(self, n: int) -> int:
        #sieve of eranthesis
        if n==0 or n==1 or n==2:
            return 0
        
        sieve=[True]*(n)
        sieve[0]=False
        sieve[1]=False
        
        for i in range(2,int(math.sqrt(n))+1):
            if sieve[i] and self.prime(i):
                for j in range(i**2,n,i):
                    sieve[j]=False
        
        cnt=0
        for i in range(1,n):
            if sieve[i]:
                cnt+=1
            
        return cnt
        
    def prime(self,n):
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True