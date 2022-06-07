class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        cnt=0
        text=text.split(' ')
        for i in text:
            flag=0
            for j in i:
                if j in brokenLetters:
                    flag=1
                    break
            if flag==0:
                cnt+=1
        return cnt
        