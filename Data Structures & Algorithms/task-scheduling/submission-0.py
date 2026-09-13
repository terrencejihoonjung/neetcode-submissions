import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)
        if len(tasks) == 1: return 1

        count = Counter(tasks)
        max_heap = list(count.values())

        heapq.heapify_max(max_heap)
        queue = deque() # append, popleft 
        time = 0

        while max_heap or queue: 
            time += 1

            if max_heap:
                freq = heapq.heappop_max(max_heap) - 1
                if freq > 0:
                    queue.append([freq, time + n])
            
            if queue and queue[0][1] == time:
                freq = queue.popleft()[0]
                heapq.heappush_max(max_heap, freq)
        
        return time





# how do we determine which task to do next? 
#   - work on the most frequent task first (greedy) -> max heap 
# how do we know when a task cooling down is ready again?
#   - need to track updated frequency of a task + the time to execute again 
#   - use a queue to track tasks that can be executed at the current time 

# use a global time variable to track the cycles ran so far 

# 1 - get frequencies of tasks 
# 2 - insert frequencies into a max heap
# 3 - iterate through max heap AND queue until both are exhausted 
#   - prioritize the max heap then check queue 
#   - when a task from a queue is being exected and has > 0 frequency still, 
#     add to max heap
