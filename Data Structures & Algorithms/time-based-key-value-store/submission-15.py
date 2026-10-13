class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tmap:
            return ""

        start, end = 0, len(self.tmap[key]) - 1
        last = ""

        while start <= end:
            middle = (start + end) // 2
            if self.tmap[key][middle][0] == timestamp:
                return self.tmap[key][middle][1]
            elif self.tmap[key][middle][0] < timestamp:
                last = self.tmap[key][middle][1]
                start = middle + 1
            else:
                end = middle - 1
        
        return last
        
