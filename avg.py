import copy
from datetime import datetime

class avg:
    
    def __init__(self, duration = "minute"):
        self.avgDuration = duration
        self.count = 0
        self.data = []
        self.time = None

    def add(self, dataList):
        if self.count == 0:
            self.data = copy.deepcopy(dataList)
            self.count = self.count + 1
            self.time = datetime.now()
            return

        for i in range(len(dataList)):
            self.data[i] = self.data[i] + dataList[i]

        self.count = self.count + 1

    def getCount(self):
        return self.count

    def getStarttime(self):
        return copy.deepcopy(self.time)

    def checkTime(self, time : datetime):
        if self.time is not None:
            if self.avgDuration == "minute" and time.minute != self.time.minute:
                return True
        return False

    def getData(self):
        self.data[:] = [elm / self.count for elm in self.data]
        self.count = 0

        return copy.deepcopy(self.data)
    
        
    