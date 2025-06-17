###
# Approach:
# - Use BFS to change the color of the starting pixel and all its connected neighbors (4-directionally)
#   that have the same original color.
# - Start with the source pixel (sr, sc), store its original color.
# - For every connected neighbor with the same original color, change it to the new color,
#   and add it to the queue.
#
# Time Complexity: O(m * n) in the worst case (visit all pixels)
# Space Complexity: O(m * n) for the queue
###
class Solution:
    def floodFill(self, image, sr, sc, color):
        if not image:
            return []
        if image[sr][sc] == color:
            return image
        initColor = image[sr][sc]
        image[sr][sc] = color
        m = len(image)
        n = len(image[0])
        queue = deque()
        queue.append((sr, sc))
        while queue:
            r,c = queue.popleft()
            ngh = [[0,1],[1,0], [0,-1], [-1,0]]
            for ng in ngh:
                nr = ng[0] + r
                nc = ng[1] + c
                if nr >= 0 and nc >= 0 and nr < m and nc < n and image[nr][nc] == initColor:
                    image[nr][nc] = color
                    queue.append((nr, nc))
        return image
    
    def main(self):
        # Test case
        image = [
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1]
        ]
        sr = 1
        sc = 1
        new_color = 2

        result = self.floodFill(image, sr, sc, new_color)
        print("Flood Filled Image:")
        for row in result:
            print(row)

# Run the test
sol = Solution()
sol.main()