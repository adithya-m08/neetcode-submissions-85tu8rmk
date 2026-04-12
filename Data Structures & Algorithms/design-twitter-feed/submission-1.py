class Twitter:

    def __init__(self):
        self.count=0
        self.tweetmap=defaultdict(list)
        self.followermap=defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count, tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followermap[userId].add(userId)

        heap=[]
        for followee in self.followermap[userId]:
            if followee in self.tweetmap:
                index=len(self.tweetmap[followee])-1
                c, tweetid=self.tweetmap[followee][index]
                heapq.heappush(heap, [c, tweetid, followee, index-1])
        res=[] 
        while heap and len(res)<10:
            c, tweetid, followee, index=heapq.heappop(heap)
            res.append(tweetid)
            if index>=0:
                count, tweetid = self.tweetmap[followee][index]
                heapq.heappush(heap, [count, tweetid, followee, index-1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followermap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followermap[followerId]:
            self.followermap[followerId].remove(followeeId)
