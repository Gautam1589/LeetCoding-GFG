class Codec:
    def __init__(self):
        self.encode_={}
        self.c='https://tinyurl.com/'

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        url=longUrl[21:].split('/')
        res=[]
        n=0
        i=0
        while True:
            for j in range(65,92):
                for k in range(97,124):
                    res.append(str(n)+str(j)+str(k))
                    res.append('/')
                    i+=1
                    if i==len(url):
                        res=self.c+''.join(res)
                        self.encode_[res]=longUrl
                        return res
            n+=1
        
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.encode_[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))