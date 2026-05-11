class Twitter:

    def __init__(self):
        self.following = {}
        self.tweets = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets:
            self.tweets[userId].append([self.timestamp, tweetId])
        else:
            self.tweets[userId] = [[self.timestamp, tweetId]]

        self.timestamp -= 1
        print("-")
        print(self.following)
        print(self.tweets)
        print(self.timestamp)
    def getNewsFeed(self, userId: int) -> List[int]:
        allFeed = []
        if userId in self.tweets:
            allFeed = self.tweets[userId].copy()

        for i in self.tweets:
            if i == userId:
                continue
            if userId in self.following and i in self.following[userId]:
                allFeed += self.tweets[i].copy()
        
        print("-")
        print(allFeed)
        heapq.heapify(allFeed)
        newsFeed = []
        while allFeed and len(newsFeed) < 10:
            mostRecent = heapq.heappop(allFeed)
            newsFeed.append(mostRecent[1])
        print(newsFeed)
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            if followeeId not in self.following[followerId]:
                self.following[followerId].append(followeeId)
        else:
            self.following[followerId] = [followeeId]
        print("-")
        print(self.following)
        print(self.tweets)
        print(self.timestamp)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            idx = self.following[followerId].index(followeeId)
            del self.following[followerId][idx]
        print("-")
        print(self.following)
        print(self.tweets)
        print(self.timestamp)
    
