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
        if len(word) == i: return node.is_word

        curr = node
        c = word[i]

        if c == ".":
            return any(self.dfs(n, word, i + 1) for n in curr.children.values())

        return c in curr.children and self.dfs(curr.children[c], word, i + 1)



# same implementation as a trie but search allows wildcard letters 
#   - probably have to do some recursive calls when we encounter wildcard letters