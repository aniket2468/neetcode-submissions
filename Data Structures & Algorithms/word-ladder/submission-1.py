class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        l = len(beginWord)
        patternMap = defaultdict(list)
        for word in wordSet:
            for i in range(l):
                pattern = word[:i]+"*"+word[i+1:]
                patternMap[pattern].append(word)
        
        q = deque([(beginWord,1)])
        visited = set([beginWord])

        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist
            for i in range(l):
                pattern = word[:i]+"*"+word[i+1:]
                for neighbour in patternMap[pattern]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        q.append((neighbour, dist + 1))
                patternMap[pattern] = []
        return 0