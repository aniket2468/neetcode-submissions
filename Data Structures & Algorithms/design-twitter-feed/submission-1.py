class Twitter:

    def __init__(self):
        self.time = 0
        self.user_tweets = defaultdict(list)
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.follow_map[userId] | {userId}

        for u in users:
            for t, tweetId in self.user_tweets[u][-10:]:
                heapq.heappush(heap, (t, tweetId))
                if len(heap) > 10:
                    heapq.heappop(heap)
        feed = []
        while heap:
            feed.append(heapq.heappop(heap)[1])
        return feed[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
