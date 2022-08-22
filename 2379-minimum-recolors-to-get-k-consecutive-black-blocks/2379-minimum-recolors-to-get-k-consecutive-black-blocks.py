import math
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_opn=0
        j=0
        while j<k:
            if blocks[j]=='W':
                min_opn+=1
            j+=1
        
        i=1
        curr=min_opn
        while j<len(blocks):
            if blocks[i-1]=='W':
                curr-=1
            if blocks[j]=='W':
                curr+=1
            min_opn=min(min_opn,curr)
            i+=1
            j+=1
        
        return min_opn