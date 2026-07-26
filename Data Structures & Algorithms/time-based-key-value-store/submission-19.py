class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map: 
            self.time_map[key] = [[timestamp, value]]
        
        else:
            self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map: return ""
        values = self.time_map[key]

        left = 0
        right = len(values) - 1

        if len(values) == 0 or values[left][0] > timestamp: return ""

        while left <= right:
            mid = (left + right) // 2
            curr = values[mid]
            print(curr)

            if curr[0] == timestamp: return curr[1]

            elif curr[0] >= timestamp: right = mid - 1
            else: left = mid + 1
        
        return values[right][1]


        
# no removing of pairs in this one 
# track a map (key -> [timestamp, value])

# for a given key, we run binary search to find value with latest timestamp matching provided one

# init: map

# set: add timestamp value pair to given key 

# get: perform binary search on key's values 
#   - if the first elemnet's timestamp is greater than the given timestamp return ""
#   - while left <= right, try to find element with timestamp == prev-timestamp
#   - return right's value 