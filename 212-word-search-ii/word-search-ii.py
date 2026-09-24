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
                res.append(curr_node.word)
                curr_node.word = None # Avoid duplicate additions
                
            board[r][c] = '#' # Mark as visited
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '#' and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)
                    
            board[r][c] = char # Restore
            
            # Optimization: prune leaf nodes to speed up future searches
            if not curr_node.children:
                parent.children.pop(char)
                
        for r in range(m):
            for c in range(n):
                if board[r][c] in root.children:
                    dfs(r, c, root)
                    
        return res


          
     
               
               
