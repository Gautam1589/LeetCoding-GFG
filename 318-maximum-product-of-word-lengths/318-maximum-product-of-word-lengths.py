class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bit_arr=[0]*len(words)
        
        for i in range(len(words)):
            for j in words[i]:
                bit_arr[i] |= 1<<(ord(j)-97)
        
        max_=0
        for i in range(len(bit_arr)-1):
            for j in range(1,len(bit_arr)):
                if not (bit_arr[i]&bit_arr[j]):
                    max_=max(len(words[i])*len(words[j]),max_)
        
        return max_
            