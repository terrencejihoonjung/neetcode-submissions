class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[timestamp, value]]
        else:
            self.store[key].append([timestamp, value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""
        
        pairs = self.store[key]

        if pairs[0][0] > timestamp: return ""

        left = 0
        right = len(pairs) - 1
        while left <= right: 
            mid = (left + right) // 2

            if pairs[mid][0] == timestamp:
                return pairs[mid][1]
            
            elif pairs[mid][0] > timestamp:
                right = mid - 1
            else:
                left = mid + 1
        
        return pairs[right][1]
        
# time only moves forward so we know that the list of values for a key is monotonically increasing
# this allows us to perform binary search on the values

# set -> we simply add the value to the key's list 
# get -> return the key-value pair with matching timestamp OR the next largest timestamp
#   - in the case there is none: we reach this case if 0th value's timestamp is larger than the     timestamp       