class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            curr=curr.children[c]
        curr.end=True
        

    def search(self, word: str) -> bool:
        curr=self.root

        def dfs(i,curr):
            if i==len(word):
                return curr.end

            c=word[i]
            if c !='.':
                if c not in curr.children:
                    return False
                return dfs(i+1, curr.children[c])
            else:
                for child in curr.children.values():
                    if dfs(i+1, child):
                        return True
                return False

        return dfs(0,curr)
            

