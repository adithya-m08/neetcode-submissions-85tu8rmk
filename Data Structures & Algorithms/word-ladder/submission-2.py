from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        adj = defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                adj[pattern].append(word)

        q = deque([(beginWord, 1)])
        visit = {beginWord}

        while q:
            word, length = q.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]

                for nei in adj[pattern]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append((nei, length + 1))

        return 0