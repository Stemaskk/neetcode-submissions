class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        array = self.hashmap[key]
        start, end = 0, len(array) - 1
        maxValid = -1

        while start <= end:
            middle = (start + end) // 2
            if array[middle][0] <= timestamp:
                maxValid = max(middle, maxValid)
                start = middle + 1

            else:
                end = middle - 1
        
        if maxValid == -1:
            return ""

        return array[maxValid][1]
