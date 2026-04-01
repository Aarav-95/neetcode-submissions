class TimeMap:

    def __init__(self):
        self.timeMap = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append((timestamp, value))
        else:
            self.timeMap[key] = [(timestamp, value)]
        # {a: [(3,b), (10,t)]}
    def get(self, key: str, timestamp: int) -> str:
        print(self.timeMap)
        if key not in self.timeMap:
            return ""
        temp = self.timeMap[key]
        if timestamp > temp[-1][0]:
            return temp[-1][1]
        if timestamp < temp[0][0]:
            return ""
        l = 0
        r = len(temp) - 1
        res = 0
        val = ""
        while r >= l:
            mid = l + ((r-l) // 2)
            if timestamp >= temp[mid][0]:
                if temp[mid][0] > res:
                    res = temp[mid][0] 
                    val = temp[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return val