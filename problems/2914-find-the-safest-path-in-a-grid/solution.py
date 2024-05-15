class Solution:
    def __init__(self):
        # Use the length + 1 of the longest path possible given the input
        # constaints as a proxy for infinity. Doing this, rather than using
        # `float("inf")`, allows typing `dist_to_theif`` as an `int` matrix.
        self.longest_path: int = 400*400 + 1


    def minimumDistanceToThief(self, grid: List[List[int]], n: int):
        """
        Use breadth first search to find the minimum Manhattan distance
        from each cell (i, j) to the nearest thief, returned as a matrix
        """

        # running list of cells to consider
        cells: List[tuple[int]] = []
        # preallocate n*n matrix of Manhatten distance to nearest thief
        dist_to_theif: List[List[int]] = [
            [0 for _ in range(n)] for _ in range(n)
        ]

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    # initial cells to consider are those with thieves
                    cells.append((i,j))
                else:
                    # to start with, any path an improvement
                    dist_to_theif[i][j] = self.longest_path

        while cells:
            x, y = cells.pop(0)
            xy_score: int = dist_to_theif[x][y]

            # consider cells left, right, above, and below respectively
            for new_x, new_y in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                # check haven't left the grid
                if 0 <= new_x < n and 0 <= new_y < n:
                    # check new path would be shorter
                    if dist_to_theif[new_x][new_y] > xy_score + 1:
                        # if so, update the shortest distance
                        dist_to_theif[new_x][new_y] = xy_score + 1
                        # and add the new cell to be considered 
                        cells.append((new_x, new_y))

        return dist_to_theif


    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        """
        The 'safeness factor' is the minimum distance to any thief,
        so we now want to maximise this safeness factor. This is
        done using Dijkstra with a heap queue so that at each stage
        the cell with the maximum safeness factor is considered. 
        """

        n: int = len(grid)

        # if the top-left or bottom right cells contain thieves,
        # any path will go through a thief so we can terminate
        if grid[0][0] or grid[n-1][n-1]: return 0

        # distance[i][j] is the min distance from grid[i][j] to a thief
        distance: List[List[int]] = self.minimumDistanceToThief(grid, n)

        # preallocate n*n boolean matrix of if (i, j) is visited
        visited: List[List[bool]] = [
            [False for _ in range(n)] for _ in range(n)
        ]

        # heap will be tupples of (safenessfactor, x, y)
        heap: List[tuple[int]] = []
        # initial cell will always be the the top left, (0, 0)
        heappush(heap, (-distance[0][0], 0, 0))

        while heap:
            # consider the largest safeness factor on the heap
            safeness, x, y = heappop(heap)
            safeness = -safeness

            # if made it to the bottom right, we're done!
            if x == n-1 and y == n-1: return safeness

            # mark current cell as visited, don't want to come back here
            visited[x][y] = True

            # consider cells left, right, above, and below respectively
            for new_x, new_y in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                # check we haven't left the grid
                if 0 <= new_x < n and 0 <= new_y < n:
                    # check we haven't already been here
                    if not visited[new_x][new_y]:
                        heappush(heap, (
                            -min(safeness, distance[new_x][new_y]),
                            new_x,
                            new_y
                        ))
                        # this cell will be returned to one last time when
                        # removed from the heap, but don't want to revist
                        # when exploring from other cells
                        visited[new_x][new_y] = True

