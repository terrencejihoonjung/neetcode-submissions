import heapq
class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.count = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.setdefault(userId, [])
        self.tweets[userId].append([self.count, tweetId])
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = [] 
        following = list(self.following[userId]) if userId in self.following else []
        following.append(userId)
        print(following)
        for user in following: 
            if user in self.tweets: tweets.extend(self.tweets[user])
        
        min_heap = []
        heapq.heapify(min_heap)
        for tweet in tweets:
            heapq.heappush(min_heap, (tweet[0], tweet[1]))
            if len(min_heap) > 10:
                heapq.heappop(min_heap)
        
        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])
        res.reverse()
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(followerId, set())
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
# use a map mapping user_id to users following 
# use another map to map user id to tweets [order, tweet_id]

# getNewsFeed:
# build a min heap using the user's and user's followees stored tweets. Maintain a min heap size of 10 at all times
