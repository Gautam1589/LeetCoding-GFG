class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        
        ans=set()
        for word in words:
            s=''
            for j in word:
                s+=morse_code[j]
            ans.add(s)
        return len(ans)