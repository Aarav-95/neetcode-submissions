class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        i = 0
        curr = self.root
        while i < len(word) and word[i] in curr.children:
            curr = curr.children[word[i]]
            i += 1
        
        while i < len(word):
            curr.children[word[i]] = Node()
            curr = curr.children[word[i]]
            i += 1
        
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        if curr.end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True

        