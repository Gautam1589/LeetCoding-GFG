class UndergroundSystem:

    def __init__(self):
        self.d1={}
        self.d2=Counter()
        self.f=Counter()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.d1[id]=(stationName,t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        s,t1=self.d1[id]
        self.d2[(s,stationName)]+=t-t1
        self.f[(s,stationName)]+=1
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        avg=0
        avg=self.d2[(startStation,endStation)]/self.f[(startStation,endStation)]
    
        return avg


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)