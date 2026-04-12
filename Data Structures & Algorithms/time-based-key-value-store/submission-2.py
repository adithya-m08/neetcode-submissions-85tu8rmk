class TimeMap:

    def __init__(self):
        self.ts=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ts[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values=self.ts[key]
        i,j=0,len(values)-1
        res=""
        while i<=j:
            m=(i+j)//2

            if values[m][1]>timestamp:
                j=m-1
            else:
                res=values[m][0]
                i=m+1
        return res