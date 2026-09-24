class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
            
        m, n = len(board), len(board[0])
        res = []
        
        def dfs(r, c, parent):
            char = board[r][c]
            curr_node = parent.children[char]
            
            if curr_node.word:
               
               
