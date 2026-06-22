class TimeMap:

    def __init__(self):
        self.store=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        values=self.store[key]

        i,j=0, len(values)-1
        res=""

        while i<=j:
            m=(i+j)//2

            if values[m][0]<=timestamp:
                res=values[m][1]
                i+=1
            else:
                j-=1
        return res