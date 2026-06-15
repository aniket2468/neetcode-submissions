class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = True
        

    def search(self, word: str) -> bool:
        def dfs(i, cur):
            for j in range(i, len(word)):
                c = word[j]
                if c == '.':
                    for child in cur:
                        if child != '#' and dfs(j + 1, cur[child]):
                            return True
                    return False
                if c not in cur:
                    return False
                cur = cur[c]
            return '#' in cur
        return dfs(0, self.root)