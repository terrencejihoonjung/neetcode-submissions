class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = [(timestamp, value)]
        else:
            self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict: return ""
        tuples = self.dict[key]
        if tuples[0][0] > timestamp: return "" 

        n = len(tuples)

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            tup = tuples[mid]

            if  tup[0] <= timestamp: 
                left = mid + 1
            else: right = mid - 1
        
        return tuples[left - 1][1]

        
# need a map that maps key to list of (timestamp, value) tuples 
# gets guarantee that a set was caled beforehand

# for a given key, perform binary search on the timestamps and return the right most value
# when setting, add the timestamp, value tuple for the given key -> O(1) 
# when getting -> O(log n) 
