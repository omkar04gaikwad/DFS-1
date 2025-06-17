###
# Approach:
# - Perform multi-source BFS from all 0s in the matrix.
# - Initialize all 0s in the queue and set non-zero cells to ∞ (unprocessed).
# - From each 0, expand in all 4 directions and update neighbors with distance = current + 1.
# - Only update a cell if the new distance is smaller.
#
# Time Complexity: O(m * n) — each cell is visited once
# Space Complexity: O(m * n) — for the queue
###
from collections import deque
class Solution:
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = float('inf')
        while queue:
            r, c = queue.popleft()
            dirs = [[0,1],[1,0], [0,-1], [-1,0]]
            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]
                if nr >= 0 and nc >= 0 and nr < m and nc < n and mat[nr][nc] != 0:
                    if mat[nr][nc] > mat[r][c] + 1:
                        mat[nr][nc] = mat[r][c] + 1
                        queue.append((nr, nc))
        return mat
    
    def main(self):
        # Test Case
        mat = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 1, 1]
        ]
        result = self.updateMatrix(mat)
        print("Updated Distance Matrix:")
        for row in result:
            print(row)

# Run
sol = Solution()
sol.main()