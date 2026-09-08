class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_word = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)

    def dfs(self, node: TrieNode, word: str, i: int) -> bool:
        if i == len(word): return node.is_word

        ch = word[i]

        if ch == ".":
            return any(self.dfs(child, word, i + 1) for child in node.children.values())
        
        return ch in node.children and self.dfs(node.children[ch], word, i + 1)

        
# search should walk through children normally 
#   - when a wildcard node is encountered, we perform recursive search on all its children
#   - else, just perform one recursive call on the next child node 