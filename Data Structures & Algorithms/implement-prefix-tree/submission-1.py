class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def walk(self, word: str) -> Optional[TrieNode]:
        curr = self.root
        for ch in word:
            if ch not in curr.children: return None
            curr = curr.children[ch]
        return curr 

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_word = True

    def search(self, word: str) -> bool:
        node = self.walk(word)
        return node is not None and node.is_word == True
        
    def startsWith(self, prefix: str) -> bool:
        return self.walk(prefix) is not None
        